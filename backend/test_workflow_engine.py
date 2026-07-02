from backend.workflows.workflow_engine import WorkflowEngine

engine = WorkflowEngine()

print("\nSequential Workflow")
workflow = engine.execute_leave_workflow(
    employee_id="EMP101",
    leave_days=5
)

print(workflow)

print("\nParallel Workflow")
print(engine.execute_parallel_tasks())

print("\nConditional Branch")
print(engine.validate_leave_balance(20,5))

print(engine.validate_leave_balance(2,5))

print("\nGet Workflow")
print(engine.get_workflow(workflow["workflow_id"]))

print("\nRollback")
print(engine.rollback(workflow["workflow_id"]))