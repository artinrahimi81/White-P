import json,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.graph_guard import STATUS_END,STATUS_START,extract_status_record,valid_task_parameter_id,validate_graph

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

if __name__=="__main__": unittest.main(verbosity=2)
