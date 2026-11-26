import json,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.graph_guard import FIXED_PARAMETER_IDS,STATUS_END,STATUS_START,derive_execution_waves,extract_status_record,fixed_ids_from_prompt,fixed_parameter_definitions_from_prompt,valid_task_parameter_id,validate_graph,validate_parameter_registry

def node(tid,deps=None,status="not_started"): return {"id":tid,"depends_on":deps or [],"status":status}
def graph_fixture(): return {"tasks":[node("WP-INIT-001"),node("WP-INIT-002",["WP-INIT-001"])]}
def done_record(tid="WP-INIT-001"):
 return {
  "schema_version":"1.0","task_id":tid,"graph_status":"done","prerequisite_reviews":[],
  "acceptance_criteria":[{"id":"ACC-001","description":"Output exists.","status":"passed","evidence":["output.md"]}],
  "actual_output_paths":["output.md"],"evidence":["output.md"],
  "execution_history":[{"attempt_id":f"{tid}-A001","started_at":"2026-11-27T10:00:00Z","ended_at":"2026-11-27T10:01:00Z","result":"succeeded","summary":"Created and checked output.","changed_files":["output.md"],"commit_sha":None,"tests":[{"command":"static output check","result":"passed","summary":"Output inspected."}],"failure_details":None,"blocked_reason":None,"reopened_reason":None,"contract_changes":[],"follow_up":"None."}],
  "execution_summary":{"attempt_count":1,"failed_attempt_count":0,"tests_passed":["static output check"],"tests_failed":[]},
  "agent_reviews":[],"consultations":[],"edge_change_log":[],"contract_revalidation":{"state":"not_required","affected_task_ids":[],"reason":None,"evidence":[]},"blocked_reason":None,"deferral":None}
def write_status(root,record):
 folder=root/"Production"/"Development"/"Tasks"/record["task_id"]; folder.mkdir(parents=True,exist_ok=True)
 raw=json.dumps(record,ensure_ascii=False,indent=2); fence=chr(96)*3
 (folder/"task-status.md").write_text("# Task Status\n\n"+STATUS_START+"\n"+fence+"json\n"+raw+"\n"+fence+"\n"+STATUS_END+"\n",encoding="utf-8")


class CentralParameterRegistryTests(unittest.TestCase):
 def write_prompt(self,root,sections):
  p=root/"Production"/"Development"/"agents"/"senior-engineer.md"
  p.parent.mkdir(parents=True,exist_ok=True)
  p.write_text("\n".join(sections),encoding="utf-8")
  return p
 def test_fixed_parameters_are_read_from_senior_prompt(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp)
   self.write_prompt(root,["## Canonical fixed-parameter registry","### execution-engineer","- EX-01 — Canonical check one.","- EX-02 — Canonical check two."])
   role_dir=root/"Production"/"Development"/"agents"
   (role_dir/"execution-engineer.md").write_text("## Fixed specialist parameters\n- EX-99 — Obsolete local check.",encoding="utf-8")
   self.assertEqual(fixed_ids_from_prompt(root,"execution-engineer"),["EX-01","EX-02"])
   self.assertEqual(fixed_parameter_definitions_from_prompt(root,"execution-engineer"),[("EX-01","Canonical check one."),("EX-02","Canonical check two.")])
 def test_missing_central_role_does_not_fall_back_to_specialist_prompt(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp)
   role_dir=root/"Production"/"Development"/"agents"
   role_dir.mkdir(parents=True)
   (role_dir/"execution-engineer.md").write_text("- EX-01 — Local-only definition.",encoding="utf-8")
   self.assertEqual(fixed_ids_from_prompt(root,"execution-engineer"),[])
 def test_registry_validator_requires_all_expected_role_parameters(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp)
   sections=["## Canonical fixed-parameter registry"]
   for role,ids in FIXED_PARAMETER_IDS.items():
    sections.append(f"### {role}")
    sections.extend(f"- {pid} — Check for {pid}." for pid in ids)
   self.write_prompt(root,sections)
   self.assertEqual(validate_parameter_registry(root),[])
   sections[sections.index("- EX-01 — Check for EX-01.")]="- EX-09 — Wrong ID."
   self.write_prompt(root,sections)
   self.assertIn("CANONICAL_PARAMETER_REGISTRY_MISMATCH",{finding.code for finding in validate_parameter_registry(root)})

class GraphStructureTests(unittest.TestCase):
 def test_valid_graph(self): self.assertEqual(validate_graph(graph_fixture()),[])
 def test_only_tasks_root_key(self):
  g=graph_fixture(); g["metadata"]={}
  self.assertIn("INVALID_GRAPH_DOCUMENT",{x.code for x in validate_graph(g)})
 def test_exact_three_key_node(self):
  g=graph_fixture(); g["tasks"][0]["title"]="forbidden"
  self.assertIn("INVALID_NODE_SHAPE",{x.code for x in validate_graph(g)})
 def test_duplicate_id(self):
  g=graph_fixture(); g["tasks"].append(node("WP-INIT-001"))
  self.assertIn("DUPLICATE_TASK_ID",{x.code for x in validate_graph(g)})
 def test_unknown_prerequisite(self):
  self.assertIn("UNKNOWN_DEPENDENCY",{x.code for x in validate_graph({"tasks":[node("WP-INIT-001",["WP-MISSING-001"])]})})
 def test_self_dependency(self):
  self.assertIn("SELF_DEPENDENCY",{x.code for x in validate_graph({"tasks":[node("WP-INIT-001",["WP-INIT-001"])]})})
 def test_duplicate_edge(self):
  g={"tasks":[node("WP-INIT-001"),node("WP-INIT-002",["WP-INIT-001","WP-INIT-001"])]}
  self.assertIn("DUPLICATE_DEPENDENCY",{x.code for x in validate_graph(g)})
 def test_cycle(self):
  g={"tasks":[node("WP-INIT-001",["WP-INIT-002"]),node("WP-INIT-002",["WP-INIT-001"])]}
  self.assertIn("DEPENDENCY_CYCLE",{x.code for x in validate_graph(g)})
 def test_deferred_final_status(self):
  self.assertEqual(validate_graph({"tasks":[node("WP-INIT-001",status="deferred_final")]}),[])
 def test_invalid_status(self):
  self.assertIn("INVALID_TASK_STATUS",{x.code for x in validate_graph({"tasks":[node("WP-INIT-001",status="almost_done")]})})

class TaskSpecificParameterIdTests(unittest.TestCase):
 def test_valid_two_digit_parameter(self): self.assertTrue(valid_task_parameter_id("SE","SE-T01"))
 def test_valid_three_digit_parameter(self): self.assertTrue(valid_task_parameter_id("QA","QA-T123"))
 def test_wrong_role_prefix(self): self.assertFalse(valid_task_parameter_id("SE","QA-T01"))
 def test_missing_or_invalid_numeric_suffix(self):
  self.assertFalse(valid_task_parameter_id("SE","SE-T"))
  self.assertFalse(valid_task_parameter_id("SE","SE-T1"))
  self.assertFalse(valid_task_parameter_id("SE","SE-T1234"))
  self.assertFalse(valid_task_parameter_id("SE","SE-TAA"))

class TaskStatusTests(unittest.TestCase):
 def test_extract_record(self):
  record=done_record(); fence=chr(96)*3
  markdown=STATUS_START+"\n"+fence+"json\n"+json.dumps(record)+"\n"+fence+"\n"+STATUS_END
  self.assertEqual(extract_status_record(markdown),record)
 def test_missing_record(self):
  with self.assertRaises(ValueError): extract_status_record("# status only")
 def test_done_requires_status_file(self):
  with tempfile.TemporaryDirectory() as td:
   errors={x.code for x in validate_graph({"tasks":[node("WP-INIT-001",status="done")]},Path(td))}
  self.assertIn("MISSING_TASK_STATUS",errors)
 def test_done_requires_actual_output_and_passing_check(self):
  graph={"tasks":[node("WP-INIT-001",status="done")]}; record=done_record()
  record["actual_output_paths"]=[]
  record["execution_history"][0]["tests"][0]["result"]="failed"
  record["execution_summary"]["tests_passed"]=[]
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); (root/"output.md").write_text("output",encoding="utf-8"); write_status(root,record)
   errors={x.code for x in validate_graph(graph,root)}
  self.assertIn("DONE_WITHOUT_OUTPUT",errors); self.assertIn("DONE_WITHOUT_PASSED_TESTS",errors)
 def test_validated_edge_needs_reason_and_evidence(self):
  graph={"tasks":[node("WP-INIT-001"),node("WP-INIT-002",["WP-INIT-001"],status="done")]}
  record=done_record("WP-INIT-002")
  record["prerequisite_reviews"]=[{"task_id":"WP-INIT-001","classification":"hard_dependency","validation_status":"validated","rationale":"","evidence":[]}]
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); (root/"output.md").write_text("output",encoding="utf-8"); write_status(root,record)
   errors={x.code for x in validate_graph(graph,root)}
  self.assertIn("VALIDATED_EDGE_WITHOUT_EVIDENCE",errors)
 def test_validated_sequencing_only_can_be_bypassed(self):
  graph={"tasks":[node("WP-INIT-001",status="not_started"),node("WP-INIT-002",["WP-INIT-001"],status="in_progress")]}
  record=done_record("WP-INIT-002")
  record.update({"graph_status":"in_progress","prerequisite_reviews":[{"task_id":"WP-INIT-001","classification":"sequencing_only","validation_status":"validated","rationale":"No output is consumed.","evidence":["prereq.md"]}],"acceptance_criteria":[],"actual_output_paths":[],"execution_history":[],"execution_summary":{"attempt_count":0,"failed_attempt_count":0,"tests_passed":[],"tests_failed":[]},"agent_reviews":[]})
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); (root/"prereq.md").write_text("review",encoding="utf-8"); write_status(root,record)
   errors={x.code for x in validate_graph(graph,root)}
  self.assertNotIn("PREREQUISITE_NOT_DONE",errors)
 def test_unreviewed_edge_cannot_be_bypassed(self):
  graph={"tasks":[node("WP-INIT-001",status="not_started"),node("WP-INIT-002",["WP-INIT-001"],status="in_progress")]}
  record=done_record("WP-INIT-002")
  record.update({"graph_status":"in_progress","prerequisite_reviews":[{"task_id":"WP-INIT-001","classification":"unreviewed","validation_status":"unreviewed","rationale":"","evidence":[]}],"acceptance_criteria":[],"actual_output_paths":[],"execution_history":[],"execution_summary":{"attempt_count":0,"failed_attempt_count":0,"tests_passed":[],"tests_failed":[]},"agent_reviews":[]})
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); write_status(root,record); errors={x.code for x in validate_graph(graph,root)}
  self.assertIn("PREREQUISITE_NOT_DONE",errors)
 def test_deferred_final_needs_full_metadata(self):
  graph={"tasks":[node("WP-INIT-001",status="deferred_final")]}; record=done_record()
  record.update({"graph_status":"deferred_final","deferral":{"reason":"No endpoint yet"}})
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); (root/"output.md").write_text("output",encoding="utf-8"); write_status(root,record)
   errors={x.code for x in validate_graph(graph,root)}
  self.assertIn("DEFERRED_FINAL_WITHOUT_METADATA",errors)
 def test_parent_path_is_rejected(self):
  graph={"tasks":[node("WP-INIT-001",status="done")]}; record=done_record()
  record["actual_output_paths"]=["../outside.md"]
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); (root/"output.md").write_text("output",encoding="utf-8"); write_status(root,record)
   errors={x.code for x in validate_graph(graph,root)}
  self.assertIn("UNSAFE_OUTPUT_PATH",errors)


class ExecutionWaveTests(unittest.TestCase):
 def test_independent_tasks_share_first_wave(self):
  graph={"tasks":[node("WP-A"),node("WP-B"),node("WP-C",["WP-A"])]}
  positions,waves=derive_execution_waves(graph)
  self.assertEqual([["WP-A","WP-B"],["WP-C"]],waves)
  self.assertEqual({"topological_order":1,"wave_id":"WAVE-001","wave_index":1},positions["WP-A"])
  self.assertEqual({"topological_order":2,"wave_id":"WAVE-001","wave_index":1},positions["WP-B"])
  self.assertEqual({"topological_order":3,"wave_id":"WAVE-002","wave_index":2},positions["WP-C"])
 def test_wave_tie_breaking_uses_graph_order(self):
  _,waves=derive_execution_waves({"tasks":[node("WP-Z"),node("WP-A"),node("WP-B",["WP-Z"])]})
  self.assertEqual([["WP-Z","WP-A"],["WP-B"]],waves)
 def test_cycle_has_no_execution_wave_plan(self):
  graph={"tasks":[node("WP-A",["WP-B"]),node("WP-B",["WP-A"])]}
  with self.assertRaises(ValueError): derive_execution_waves(graph)

class Schema11TaskStatusTests(unittest.TestCase):
 def make_record(self):
  record=done_record(); record["schema_version"]="1.1"
  record["source_baseline"]={
   "source_path":"Production/task-decomposition/main-document.md","source_version":"not_versioned",
   "main_commit_sha":"1"*40,"source_blob_sha":"2"*40,"graph_blob_sha":"3"*40,
   "catalog_blob_sha":"4"*40,"captured_at":"2026-11-27T00:00:00Z"}
  positions,_=derive_execution_waves({"tasks":[node("WP-INIT-001",status="done")]})
  record["execution_plan"]={**positions["WP-INIT-001"],"scheduling_mode":"sequential_default",
   "parallelism_authorized":False,"parallelism_reason":"Serial task execution remains the default.",
   "parallelism_evidence":[]}
  record["requirement_change_register"]=[]
  record["affected_task_reconciliation"]=[]
  return record
 def test_schema11_requires_source_baseline_and_execution_plan(self):
  graph={"tasks":[node("WP-INIT-001",status="done")]}
  record=self.make_record(); record.pop("source_baseline"); record.pop("execution_plan")
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); (root/"output.md").write_text("output",encoding="utf-8"); write_status(root,record)
   errors={x.code for x in validate_graph(graph,root)}
  self.assertIn("MISSING_SOURCE_BASELINE",errors); self.assertIn("MISSING_EXECUTION_PLAN",errors)
 def test_schema11_rejects_incorrect_wave(self):
  graph={"tasks":[node("WP-INIT-001",status="done")]}
  record=self.make_record(); record["execution_plan"]["wave_id"]="WAVE-009"
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); (root/"output.md").write_text("output",encoding="utf-8"); write_status(root,record)
   errors={x.code for x in validate_graph(graph,root)}
  self.assertIn("EXECUTION_WAVE_MISMATCH",errors)
 def test_impact_mapping_requires_complete_task_reconciliation(self):
  graph={"tasks":[node("WP-INIT-001",status="done"),node("WP-INIT-002",["WP-INIT-001"],status="done")]}
  record=self.make_record()
  record["requirement_change_register"]=[{
   "change_id":"CHG-20261127-001","recorded_at":"2026-11-27T00:00:00Z",
   "source_version_before":"1.0","source_version_after":"1.1",
   "changed_requirement_ids":["REQ-001"],"change_summary":"A shared contract changed.",
   "reason":"Test fixture.","evidence":["change.md"],"affected_task_ids":["WP-INIT-002"],
   "recorded_by":"senior-engineer","status":"impact_mapped"}]
  record["affected_task_reconciliation"]=[{
   "change_id":"CHG-20261127-001","task_id":"WP-INIT-002","baseline_status":"done","current_status":"done",
   "impact_classification":"contract","decision":"re_review_required","review_status":"reviewed",
   "revalidation_status":"required","status_changed":False,"status_transition":None,
   "task_status_path_exists":False,"update_task_ids":[],"evidence":["change.md"],
   "reviewed_by":"senior-engineer","reviewed_at":"2026-11-27T00:00:00Z"}]
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); (root/"output.md").write_text("output",encoding="utf-8"); (root/"change.md").write_text("change",encoding="utf-8"); write_status(root,record)
   errors={x.code for x in validate_graph(graph,root)}
  self.assertNotIn("RECONCILIATION_SET_MISMATCH",errors)
  self.assertNotIn("REVIEWED_RECONCILIATION_WITHOUT_EVIDENCE",errors)
 def test_changed_status_requires_explicit_evidence(self):
  graph={"tasks":[node("WP-INIT-001",status="done"),node("WP-INIT-002",["WP-INIT-001"],status="blocked")]}
  record=self.make_record()
  record["requirement_change_register"]=[{
   "change_id":"CHG-20261127-001","recorded_at":"2026-11-27T00:00:00Z",
   "source_version_before":"1.0","source_version_after":"1.1",
   "changed_requirement_ids":["REQ-001"],"change_summary":"A shared contract changed.",
   "reason":"Test fixture.","evidence":["change.md"],"affected_task_ids":["WP-INIT-002"],
   "recorded_by":"senior-engineer","status":"impact_mapped"}]
  record["affected_task_reconciliation"]=[{
   "change_id":"CHG-20261127-001","task_id":"WP-INIT-002","baseline_status":"done","current_status":"blocked",
   "impact_classification":"contract","decision":"blocked","review_status":"pending",
   "revalidation_status":"required","status_changed":True,"status_transition":None,
   "task_status_path_exists":False,"update_task_ids":[],"evidence":[],
   "reviewed_by":"senior-engineer","reviewed_at":"2026-11-27T00:00:00Z"}]
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); (root/"output.md").write_text("output",encoding="utf-8"); (root/"change.md").write_text("change",encoding="utf-8"); write_status(root,record)
   errors={x.code for x in validate_graph(graph,root)}
  self.assertIn("INCOMPLETE_RECONCILIATION_TRANSITION",errors)

if __name__=="__main__": unittest.main(verbosity=2)
