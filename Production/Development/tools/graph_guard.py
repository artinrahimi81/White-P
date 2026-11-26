#!/usr/bin/env python3
"""Validate White-P's minimal DAG and detailed per-task execution records."""
from __future__ import annotations
import argparse, json, re, sys
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

GRAPH_STATUSES={"not_started","in_progress","done","blocked","deferred_final"}
EDGE_CLASSES={"hard_dependency","contract_or_interface_dependency","sequencing_only","unreviewed"}
EDGE_STATES={"unreviewed","validated","disputed"}
PARAMETER_STATES={"pending","passed","issue_found","not_applicable","needs_consultation"}
AGENT_STATES={"not_scheduled","queued","active","completed","not_applicable","blocked"}
ATTEMPT_RESULTS={"succeeded","failed","partial","blocked","reopened"}
EXECUTION_MODES={"not_run","same_assistant_sequential_role_scoped_pass","independent_agent"}
CONSULTATION_STATES={"requested","answered","accepted","rejected","unresolved"}
REVALIDATION_STATES={"not_required","required","in_review","passed","failed"}
STATUS_START="<!-- WHITEP_TASK_STATUS_RECORD_START -->"
STATUS_END="<!-- WHITEP_TASK_STATUS_RECORD_END -->"
ROLE_IDS=("senior-engineer","execution-engineer","qa-testing-engineer","safety-engineer","project-structure-engineer","design-engineer","ux-interaction-engineer","feasibility-engineer","idea-alignment-engineer","project-mapping-engineer")
BASE_DOCUMENT_ROLES={"safety-engineer","project-structure-engineer","design-engineer","ux-interaction-engineer","project-mapping-engineer"}
FIXED_PARAMETER_IDS={
 "senior-engineer":[f"SE-{i:02d}" for i in range(1,8)],
 "execution-engineer":[f"EX-{i:02d}" for i in range(1,8)],
 "qa-testing-engineer":[f"QA-{i:02d}" for i in range(1,9)],
 "safety-engineer":[f"SAF-{i:02d}" for i in range(1,8)],
 "project-structure-engineer":[f"PS-{i:02d}" for i in range(1,8)],
 "design-engineer":[f"DE-{i:02d}" for i in range(1,9)],
 "ux-interaction-engineer":[f"UX-{i:02d}" for i in range(1,9)],
 "feasibility-engineer":[f"FE-{i:02d}" for i in range(1,8)],
 "idea-alignment-engineer":[f"IA-{i:02d}" for i in range(1,7)],
 "project-mapping-engineer":[f"PM-{i:02d}" for i in range(1,8)],
}
CODE_SUFFIXES={".py",".cs",".kt",".java",".js",".ts",".tsx",".jsx",".cpp",".c",".h",".hpp",".go",".rs",".swift",".sql"}
PLACEHOLDER_PATTERNS=(
 (re.compile(r"\bTODO\b"),"TODO marker"),
 (re.compile(r"\bNotImplementedException\b"),"NotImplementedException"),
 (re.compile(r"\bNotImplementedError\b"),"NotImplementedError"),
 (re.compile(r"\bmock implementation\b",re.I),"mock implementation"),
 (re.compile(r"\bplaceholder implementation\b",re.I),"placeholder implementation"),
 (re.compile(r"\bsimulated response\b",re.I),"simulated response"),
)

@dataclass(frozen=True)
class Finding:
 severity:str
 code:str
 message:str
 def __str__(self): return f"{self.severity} {self.code}: {self.message}"

def extract_status_record(markdown:str)->dict[str,Any]:
 if markdown.count(STATUS_START)!=1 or markdown.count(STATUS_END)!=1:
  raise ValueError("task-status.md must contain exactly one canonical execution record block")
 body=markdown.split(STATUS_START,1)[1].split(STATUS_END,1)[0].strip()
 fence=chr(96)*3
 if body.startswith(fence+"json"):
  body=body[len(fence+"json"):].strip()
  if body.endswith(fence): body=body[:-3].strip()
 record=json.loads(body)
 if not isinstance(record,dict): raise ValueError("canonical task-status record must be a JSON object")
 return record

def safe_repo_file(root:Path,raw:Any):
 if not isinstance(raw,str) or not raw.strip(): return None,"path must be non-empty text"
 if "\\" in raw: return None,"use repository-relative POSIX paths"
 p=PurePosixPath(raw)
 if p.is_absolute() or any(x in {"",".",".."} for x in p.parts): return None,"absolute, dot and parent-traversal paths are forbidden"
 candidate=(root/Path(*p.parts)).resolve()
 try: candidate.relative_to(root.resolve())
 except ValueError: return None,"path escapes repository root"
 return candidate,None

def evidence_item(item:Any,root:Path,out:list[Finding],ctx:str):
 if not isinstance(item,str) or not item.strip():
  out.append(Finding("ERROR","INVALID_EVIDENCE",f"{ctx}: evidence item must be non-empty text.")); return
 if "://" in item:
  if not item.startswith("https://"): out.append(Finding("ERROR","INVALID_EVIDENCE_URL",f"{ctx}: external evidence must use HTTPS: {item!r}."))
  return
 path,problem=safe_repo_file(root,item)
 if problem: out.append(Finding("ERROR","UNSAFE_EVIDENCE_PATH",f"{ctx}: {item!r}: {problem}.")); return
 if path is None or not path.is_file(): out.append(Finding("ERROR","MISSING_EVIDENCE_FILE",f"{ctx}: evidence file not found: {item!r}."))

def fixed_ids_from_prompt(root:Path,role:str)->list[str]:
 p=root/"Production"/"Development"/"agents"/f"{role}.md"
 try: content=p.read_text(encoding="utf-8")
 except (OSError,UnicodeError): return FIXED_PARAMETER_IDS[role]
 ids=re.findall(r"^\s*-\s+([A-Z]{2,3}-\d{2})\s*[—:-]",content,re.M)
 return ids or FIXED_PARAMETER_IDS[role]

def validate_record(task,by_id,record,markdown,root,out):
 tid=task["id"]; ctx=f"{tid} task-status"
 if record.get("schema_version")!="1.0": out.append(Finding("ERROR","STATUS_SCHEMA_VERSION",f"{ctx}: schema_version must be '1.0'."))
 if record.get("task_id")!=tid: out.append(Finding("ERROR","STATUS_TASK_ID_MISMATCH",f"{ctx}: record task_id differs from graph."))
 if record.get("graph_status")!=task.get("status"): out.append(Finding("ERROR","STATUS_GRAPH_STATE_MISMATCH",f"{ctx}: record graph_status differs from graph."))

 reviews=record.get("prerequisite_reviews")
 if not isinstance(reviews,list):
  out.append(Finding("ERROR","INVALID_PREREQUISITE_REVIEWS",f"{ctx}: prerequisite_reviews must be an array.")); reviews=[]
 review_by_id={}
 for item in reviews:
  if not isinstance(item,dict):
   out.append(Finding("ERROR","INVALID_EDGE_REVIEW",f"{ctx}: edge reviews must be objects.")); continue
  pred=item.get("task_id")
  if not isinstance(pred,str) or pred in review_by_id:
   out.append(Finding("ERROR","DUPLICATE_EDGE_REVIEW",f"{ctx}: invalid/duplicate prerequisite review {pred!r}.")); continue
  review_by_id[pred]=item
  if item.get("classification") not in EDGE_CLASSES: out.append(Finding("ERROR","INVALID_EDGE_CLASSIFICATION",f"{ctx}: {pred} has invalid classification."))
  state=item.get("validation_status")
  if state not in EDGE_STATES: out.append(Finding("ERROR","INVALID_EDGE_VALIDATION_STATUS",f"{ctx}: {pred} has invalid validation status."))
  rationale=item.get("rationale"); ev=item.get("evidence",[])
  if state=="validated" and (not isinstance(rationale,str) or not rationale.strip() or not isinstance(ev,list) or not ev):
   out.append(Finding("ERROR","VALIDATED_EDGE_WITHOUT_EVIDENCE",f"{ctx}: {pred} is validated without rationale/evidence."))
  if state=="disputed" and not str(rationale or "").strip():
   out.append(Finding("ERROR","DISPUTED_EDGE_WITHOUT_REASON",f"{ctx}: disputed edge {pred} needs a reason."))
  for x in ev if isinstance(ev,list) else []: evidence_item(x,root,out,f"{ctx} edge {pred}")
 expected=set(task.get("depends_on",[])); actual=set(review_by_id)
 if expected!=actual:
  out.append(Finding("ERROR","EDGE_REVIEW_SET_MISMATCH",f"{ctx}: missing reviews={sorted(expected-actual)}; extra={sorted(actual-expected)}."))
 if task["status"] in {"in_progress","done"}:
  for pred in task.get("depends_on",[]):
   review=review_by_id.get(pred); parent=by_id.get(pred)
   if review is None or parent is None: continue
   cls=review.get("classification"); state=review.get("validation_status")
   if state=="disputed": out.append(Finding("ERROR","DISPUTED_PREREQUISITE",f"{ctx}: disputed prerequisite {pred} must be resolved."))
   elif cls=="sequencing_only" and state=="validated": pass
   elif parent.get("status")!="done": out.append(Finding("ERROR","PREREQUISITE_NOT_DONE",f"{ctx}: prerequisite {pred} is {parent.get('status')!r}, not done."))
   if task["status"]=="done" and state!="validated": out.append(Finding("ERROR","DONE_WITH_UNREVIEWED_EDGE",f"{ctx}: prerequisite {pred} must be validated."))

 criteria=record.get("acceptance_criteria")
 if not isinstance(criteria,list):
  out.append(Finding("ERROR","INVALID_ACCEPTANCE_CRITERIA",f"{ctx}: acceptance_criteria must be an array.")); criteria=[]
 seen=set()
 for c in criteria:
  if not isinstance(c,dict): out.append(Finding("ERROR","INVALID_ACCEPTANCE_ITEM",f"{ctx}: acceptance entries must be objects.")); continue
  cid=c.get("id")
  if not isinstance(cid,str) or not cid or cid in seen: out.append(Finding("ERROR","DUPLICATE_ACCEPTANCE_ID",f"{ctx}: invalid/duplicate acceptance ID {cid!r}."))
  seen.add(cid)
  state=c.get("status")
  if state not in PARAMETER_STATES: out.append(Finding("ERROR","INVALID_ACCEPTANCE_STATUS",f"{ctx}: {cid!r} has invalid status."))
  if state=="passed":
   ev=c.get("evidence",[])
   if not isinstance(ev,list) or not ev: out.append(Finding("ERROR","PASSED_ACCEPTANCE_WITHOUT_EVIDENCE",f"{ctx}: {cid} passed without evidence."))
   else:
    for x in ev: evidence_item(x,root,out,f"{ctx} acceptance {cid}")
  if state=="not_applicable" and not str(c.get("rationale","")).strip():
   out.append(Finding("ERROR","ACCEPTANCE_NA_WITHOUT_REASON",f"{ctx}: {cid} is not_applicable without reason."))
 if task["status"]=="done":
  if not criteria: out.append(Finding("ERROR","DONE_WITHOUT_ACCEPTANCE",f"{ctx}: no acceptance criteria."))
  for c in criteria:
   if isinstance(c,dict) and c.get("status") not in {"passed","not_applicable"}:
    out.append(Finding("ERROR","DONE_WITH_UNPASSED_ACCEPTANCE",f"{ctx}: {c.get('id')} is not accepted."))

 actual_paths=record.get("actual_output_paths")
 if not isinstance(actual_paths,list):
  out.append(Finding("ERROR","INVALID_ACTUAL_OUTPUTS",f"{ctx}: actual_output_paths must be an array.")); actual_paths=[]
 seen_paths=set(); code_outputs=[]
 for raw in actual_paths:
  path,problem=safe_repo_file(root,raw)
  if problem: out.append(Finding("ERROR","UNSAFE_OUTPUT_PATH",f"{ctx}: {raw!r}: {problem}.")); continue
  if raw in seen_paths: out.append(Finding("ERROR","DUPLICATE_OUTPUT_PATH",f"{ctx}: duplicate output {raw!r}.")); continue
  seen_paths.add(raw)
  if path is None or not path.is_file(): out.append(Finding("ERROR","MISSING_OUTPUT_FILE",f"{ctx}: output file not found: {raw!r}."))
  elif path.suffix.lower() in CODE_SUFFIXES and not raw.startswith(("tests/","test/")):
   code_outputs.append(path)
   try: text=path.read_text(encoding="utf-8")
   except (OSError,UnicodeError) as exc:
    out.append(Finding("ERROR","UNREADABLE_OUTPUT_FILE",f"{ctx}: cannot inspect {raw!r}: {exc}.")); continue
   for pattern,label in PLACEHOLDER_PATTERNS:
    if pattern.search(text): out.append(Finding("ERROR","DONE_WITH_PLACEHOLDER_IMPLEMENTATION",f"{ctx}: {raw!r} contains {label}."))
 if task["status"]=="done" and not actual_paths: out.append(Finding("ERROR","DONE_WITHOUT_OUTPUT",f"{ctx}: done needs a verified actual output file."))

 evidence=record.get("evidence")
 if not isinstance(evidence,list):
  out.append(Finding("ERROR","INVALID_EVIDENCE_LIST",f"{ctx}: evidence must be an array.")); evidence=[]
 for x in evidence: evidence_item(x,root,out,ctx)
 if task["status"]=="done" and not evidence: out.append(Finding("ERROR","DONE_WITHOUT_EVIDENCE",f"{ctx}: done needs reviewable evidence."))

 history=record.get("execution_history")
 if not isinstance(history,list):
  out.append(Finding("ERROR","INVALID_EXECUTION_HISTORY",f"{ctx}: execution_history must be an array.")); history=[]
 attempt_ids=set(); successful=[]; failed_count=0; passed_tests=[]; failed_tests=[]
 for attempt in history:
  if not isinstance(attempt,dict): out.append(Finding("ERROR","INVALID_ATTEMPT",f"{ctx}: attempts must be objects.")); continue
  aid=attempt.get("attempt_id")
  if not isinstance(aid,str) or not aid or aid in attempt_ids: out.append(Finding("ERROR","DUPLICATE_ATTEMPT_ID",f"{ctx}: invalid/duplicate attempt ID {aid!r}."))
  attempt_ids.add(aid)
  result=attempt.get("result")
  if result not in ATTEMPT_RESULTS: out.append(Finding("ERROR","INVALID_ATTEMPT_RESULT",f"{ctx}: attempt {aid!r} has invalid result."))
  if result=="failed": failed_count+=1
  if result=="succeeded": successful.append(attempt)
  for field in ("started_at","ended_at","summary","changed_files","tests","follow_up","failure_details","blocked_reason","reopened_reason","contract_changes"):
   if field not in attempt: out.append(Finding("ERROR","INCOMPLETE_ATTEMPT",f"{ctx}: attempt {aid!r} missing {field}."))
  if not isinstance(attempt.get("changed_files",[]),list): out.append(Finding("ERROR","INVALID_CHANGED_FILES",f"{ctx}: attempt {aid!r} changed_files must be an array."))
  tests=attempt.get("tests",[])
  if not isinstance(tests,list):
   out.append(Finding("ERROR","INVALID_ATTEMPT_TESTS",f"{ctx}: attempt {aid!r} tests must be an array.")); tests=[]
  for test in tests:
   if not isinstance(test,dict) or not isinstance(test.get("command"),str) or test.get("result") not in {"passed","failed","not_run"}:
    out.append(Finding("ERROR","INVALID_TEST_RESULT",f"{ctx}: attempt {aid!r} has malformed test/check.")); continue
   if test["result"]=="passed": passed_tests.append(test["command"])
   elif test["result"]=="failed": failed_tests.append(test["command"])
 summary=record.get("execution_summary")
 if not isinstance(summary,dict): out.append(Finding("ERROR","INVALID_EXECUTION_SUMMARY",f"{ctx}: execution_summary must be an object.")); summary={}
 if summary.get("attempt_count")!=len(history): out.append(Finding("ERROR","ATTEMPT_COUNT_MISMATCH",f"{ctx}: attempt_count disagrees with history."))
 if summary.get("failed_attempt_count")!=failed_count: out.append(Finding("ERROR","FAILED_ATTEMPT_COUNT_MISMATCH",f"{ctx}: failed_attempt_count disagrees with history."))
 if task["status"]=="done":
  if not successful: out.append(Finding("ERROR","DONE_WITHOUT_SUCCESSFUL_ATTEMPT",f"{ctx}: no succeeded attempt recorded."))
  if not passed_tests: out.append(Finding("ERROR","DONE_WITHOUT_PASSED_TESTS",f"{ctx}: no passing test/check recorded."))
 if summary.get("tests_passed",[])!=list(dict.fromkeys(passed_tests)): out.append(Finding("ERROR","PASSED_TEST_SUMMARY_MISMATCH",f"{ctx}: tests_passed summary disagrees with history."))
 if summary.get("tests_failed",[])!=list(dict.fromkeys(failed_tests)): out.append(Finding("ERROR","FAILED_TEST_SUMMARY_MISMATCH",f"{ctx}: tests_failed summary disagrees with history."))

 agents=record.get("agent_reviews")
 if not isinstance(agents,list): out.append(Finding("ERROR","INVALID_AGENT_REVIEWS",f"{ctx}: agent_reviews must be an array.")); agents=[]
 agents_by_role={}
 for agent in agents:
  if not isinstance(agent,dict): out.append(Finding("ERROR","INVALID_AGENT_REVIEW",f"{ctx}: role reviews must be objects.")); continue
  role=agent.get("role_id")
  if role not in ROLE_IDS or role in agents_by_role: out.append(Finding("ERROR","INVALID_AGENT_ROLE",f"{ctx}: unknown/duplicate role {role!r}.")); continue
  agents_by_role[role]=agent
  state=agent.get("state"); activation=agent.get("normal_activation_count"); mode=agent.get("execution_mode")
  if state not in AGENT_STATES: out.append(Finding("ERROR","INVALID_AGENT_STATE",f"{ctx}: {role} has invalid state."))
  if activation not in {0,1}: out.append(Finding("ERROR","INVALID_ACTIVATION_COUNT",f"{ctx}: {role} activation_count must be 0 or 1."))
  if mode not in EXECUTION_MODES: out.append(Finding("ERROR","INVALID_EXECUTION_MODE",f"{ctx}: {role} has invalid execution_mode."))
  if state=="completed" and (activation!=1 or mode=="not_run"): out.append(Finding("ERROR","COMPLETED_AGENT_LIFECYCLE",f"{ctx}: completed role {role} requires one activation and execution mode."))
  if state=="not_applicable" and (activation!=0 or mode!="not_run"): out.append(Finding("ERROR","NA_AGENT_LIFECYCLE",f"{ctx}: N/A role {role} requires zero activations and not_run."))
  if state=="not_applicable" and not str(agent.get("not_applicable_reason","")).strip(): out.append(Finding("ERROR","NA_AGENT_WITHOUT_REASON",f"{ctx}: {role} needs a reason."))
  if state=="completed":
   expected=fixed_ids_from_prompt(root,role); actual=agent.get("fixed_parameter_ids",[])
   if actual!=expected: out.append(Finding("ERROR","FIXED_PARAMETER_REGISTER_MISMATCH",f"{ctx}: {role} fixed IDs must be {expected}."))
   missing=[pid for pid in expected if not re.search(rf"\b{re.escape(pid)}\b",markdown)]
   if missing: out.append(Finding("ERROR","FIXED_PARAMETERS_NOT_COPIED",f"{ctx}: {role} missing fixed checks {missing}."))
   task_ids=agent.get("task_specific_parameter_ids",[])
   if not isinstance(task_ids,list) or len(task_ids)!=len(set(task_ids)): out.append(Finding("ERROR","INVALID_TASK_PARAMETER_IDS",f"{ctx}: {role} task-specific IDs must be unique."))
   else:
    prefix=expected[0].split("-")[0]
    for pid in task_ids:
     if not isinstance(pid,str) or not re.fullmatch(rf"{re.escape(prefix)}-T\d{2,3}",pid) or not re.search(rf"\b{re.escape(pid)}\b",markdown):
      out.append(Finding("ERROR","TASK_PARAMETERS_NOT_COPIED",f"{ctx}: {role} task-specific ID {pid!r} is invalid or missing."))
   log,problem=safe_repo_file(root,agent.get("work_log_path"))
   if problem or log is None or not log.is_file(): out.append(Finding("ERROR","MISSING_AGENT_WORK_LOG",f"{ctx}: {role} work log is missing or unsafe."))
   dest=agent.get("base_document_destination"); allowed={f"Production/Development/base-documents/{name}" for name in BASE_DOCUMENT_ROLES}
   if not isinstance(dest,str) or dest.rstrip("/") not in allowed: out.append(Finding("ERROR","INVALID_BASE_DOCUMENT_DESTINATION",f"{ctx}: {role} must use one of five baseline folders."))
   else:
    for name in ("task-reports.md","overall-vision.md"):
     p,problem=safe_repo_file(root,f"{dest.rstrip('/')}/{name}")
     if problem or p is None or not p.is_file(): out.append(Finding("ERROR","MISSING_BASE_DOCUMENT",f"{ctx}: {role} destination lacks {name}."))
 if set(agents_by_role)!=set(ROLE_IDS): out.append(Finding("ERROR","AGENT_ROLE_SET_MISMATCH",f"{ctx}: missing roles {sorted(set(ROLE_IDS)-set(agents_by_role))}."))
 if sum(1 for x in agents if isinstance(x,dict) and x.get("state")=="active")>1: out.append(Finding("ERROR","MULTIPLE_ACTIVE_AGENTS",f"{ctx}: only one normal specialist may be active."))

 consultations=record.get("consultations",[])
 if not isinstance(consultations,list): out.append(Finding("ERROR","INVALID_CONSULTATIONS",f"{ctx}: consultations must be an array.")); consultations=[]
 cids=set()
 for item in consultations:
  if not isinstance(item,dict): out.append(Finding("ERROR","INVALID_CONSULTATION",f"{ctx}: entries must be objects.")); continue
  cid=item.get("id")
  if not isinstance(cid,str) or not cid.startswith(f"CONS-{tid}-") or cid in cids: out.append(Finding("ERROR","INVALID_CONSULTATION_ID",f"{ctx}: invalid/duplicate ID {cid!r}."))
  cids.add(cid)
  if item.get("state") not in CONSULTATION_STATES: out.append(Finding("ERROR","INVALID_CONSULTATION_STATE",f"{ctx}: {cid!r} has invalid state."))
  for field in ("requester","recipient","question","reason","requested_answer","response","response_evidence","requester_decision","result"):
   if field not in item: out.append(Finding("ERROR","INCOMPLETE_CONSULTATION",f"{ctx}: {cid!r} missing {field}."))
 changes=record.get("edge_change_log",[])
 if not isinstance(changes,list): out.append(Finding("ERROR","INVALID_EDGE_CHANGE_LOG",f"{ctx}: edge_change_log must be an array.")); changes=[]
 for change in changes:
  required=("changed_at","edge_from","edge_to","old_classification","new_classification","reason","evidence","reviewed_by")
  if not isinstance(change,dict) or not all(x in change for x in required): out.append(Finding("ERROR","INCOMPLETE_EDGE_CHANGE",f"{ctx}: change log entry lacks required fields."))
 contract=record.get("contract_revalidation",{})
 if not isinstance(contract,dict) or contract.get("state","not_required") not in REVALIDATION_STATES: out.append(Finding("ERROR","INVALID_CONTRACT_REVALIDATION",f"{ctx}: invalid state."))
 elif task["status"]=="done" and contract.get("state") in {"required","in_review","failed"}: out.append(Finding("ERROR","DONE_WITH_PENDING_CONTRACT_REVALIDATION",f"{ctx}: revalidation is incomplete."))
 if task["status"]=="blocked" and not str(record.get("blocked_reason","")).strip(): out.append(Finding("ERROR","BLOCKED_WITHOUT_REASON",f"{ctx}: blocked task needs a blocker."))
 if task["status"]=="deferred_final":
  d=record.get("deferral")
  if not isinstance(d,dict) or not all(str(d.get(k,"")).strip() for k in ("reason","start_condition","final_stage")):
   out.append(Finding("ERROR","DEFERRED_FINAL_WITHOUT_METADATA",f"{ctx}: deferred_final requires reason, start_condition and final_stage."))
 if code_outputs and task["status"]=="done" and not any(isinstance(x,str) and (x.startswith("tests/") or x.startswith("test/")) for x in evidence):
  out.append(Finding("ERROR","DONE_WITHOUT_TEST_SOURCE_EVIDENCE",f"{ctx}: code outputs require test source evidence under tests/ or test/."))


def validate_graph(graph:Any,repo_root:Path|None=None)->list[Finding]:
 out=[]
 if not isinstance(graph,dict) or set(graph)!={"tasks"} or not isinstance(graph.get("tasks"),list):
  return [Finding("ERROR","INVALID_GRAPH_DOCUMENT","graph must contain only a tasks array.")]
 tasks=graph["tasks"]; ids=[]; by_id={}
 for index,node in enumerate(tasks):
  if not isinstance(node,dict): out.append(Finding("ERROR","INVALID_NODE",f"Task index {index} is not an object.")); continue
  if set(node)!={"id","depends_on","status"}: out.append(Finding("ERROR","INVALID_NODE_SHAPE",f"Task index {index} must have exactly id, depends_on, status.")); continue
  tid=node.get("id")
  if not isinstance(tid,str) or not tid.strip() or any(x.isspace() for x in tid): out.append(Finding("ERROR","INVALID_TASK_ID",f"Task index {index} has invalid ID {tid!r}.")); continue
  if tid in by_id: out.append(Finding("ERROR","DUPLICATE_TASK_ID",f"Task ID {tid!r} is duplicated.")); continue
  by_id[tid]=node; ids.append(tid)
  if node.get("status") not in GRAPH_STATUSES: out.append(Finding("ERROR","INVALID_TASK_STATUS",f"{tid}: unsupported status {node.get('status')!r}."))
  deps=node.get("depends_on")
  if not isinstance(deps,list) or any(not isinstance(x,str) or not x.strip() for x in deps): out.append(Finding("ERROR","INVALID_DEPENDS_ON",f"{tid}: depends_on must be an array of task IDs.")); continue
  if len(deps)!=len(set(deps)): out.append(Finding("ERROR","DUPLICATE_DEPENDENCY",f"{tid}: duplicate prerequisite IDs."))
  if tid in deps: out.append(Finding("ERROR","SELF_DEPENDENCY",f"{tid}: self-dependency is forbidden."))
  for dep in deps:
   if dep not in {x.get("id") for x in tasks if isinstance(x,dict)}: out.append(Finding("ERROR","UNKNOWN_DEPENDENCY",f"{tid}: prerequisite {dep!r} is unknown."))
 indegree={tid:0 for tid in ids}; adjacency=defaultdict(list)
 for tid,node in by_id.items():
  for dep in node.get("depends_on",[]) if isinstance(node.get("depends_on"),list) else []:
   if dep in by_id and tid!=dep: adjacency[dep].append(tid); indegree[tid]+=1
 q=deque(tid for tid,n in indegree.items() if n==0); visited=0
 while q:
  cur=q.popleft(); visited+=1
  for target in adjacency[cur]:
   indegree[target]-=1
   if indegree[target]==0: q.append(target)
 if visited!=len(by_id): out.append(Finding("ERROR","DEPENDENCY_CYCLE","Dependency graph contains a cycle."))
 if repo_root is not None:
  for tid,node in by_id.items():
   status_path=repo_root/"Production"/"Development"/"Tasks"/tid/"task-status.md"
   if node.get("status") in {"in_progress","done","blocked","deferred_final"} or status_path.is_file():
    if not status_path.is_file(): out.append(Finding("ERROR","MISSING_TASK_STATUS",f"{tid}: task-status.md is required.")); continue
    try: markdown=status_path.read_text(encoding="utf-8"); record=extract_status_record(markdown)
    except (OSError,UnicodeError,ValueError,json.JSONDecodeError) as exc: out.append(Finding("ERROR","TASK_STATUS_READ",f"{tid}: {exc}.")); continue
    validate_record(node,by_id,record,markdown,repo_root.resolve(),out)
 return out

def main(argv=None):
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument("graph",type=Path,help="Path to dependency-graph.json")
 parser.add_argument("--repo-root",type=Path,help="Validate task-status records and actual outputs against this checkout")
 parser.add_argument("--strict",action="store_true",help="Treat warnings as failures")
 args=parser.parse_args(argv)
 try: graph=json.loads(args.graph.read_text(encoding="utf-8"))
 except (OSError,UnicodeError,json.JSONDecodeError) as exc: print(f"ERROR GRAPH_READ: {exc}",file=sys.stderr); return 2
 findings=validate_graph(graph,args.repo_root.resolve() if args.repo_root else None)
 count=len(graph.get("tasks",[])) if isinstance(graph,dict) and isinstance(graph.get("tasks"),list) else 0
 edges=sum(len(n.get("depends_on",[])) for n in graph.get("tasks",[]) if isinstance(n,dict) and isinstance(n.get("depends_on"),list)) if isinstance(graph,dict) else 0
 print(f"Graph guard: {count} tasks, {edges} direct dependency edges.")
 for f in findings: print(f)
 errors=sum(x.severity=="ERROR" for x in findings); warnings=sum(x.severity=="WARNING" for x in findings)
 print(f"Result: {errors} error(s), {warnings} warning(s).")
 return 1 if errors or (args.strict and warnings) else 0

if __name__=="__main__": raise SystemExit(main())
