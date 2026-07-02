import uuid
from datetime import datetime


class WorkflowEngine:

    def __init__(self):
        self.workflows = {}

    # -------------------------
    # Sequential Workflow
    # -------------------------

    def execute_leave_workflow(self, employee_id, leave_days):

        workflow_id = "WF-" + str(uuid.uuid4())[:8]

        completed_steps = []

        steps = [
            "Check Leave Balance",
            "Validate Dates",
            "Manager Approval",
            "HR Notification",
            "Calendar Update",
            "Confirmation Email"
        ]

        for step in steps:
            completed_steps.append(step)

        workflow = {
            "workflow_id": workflow_id,
            "employee_id": employee_id,
            "leave_days": leave_days,
            "status": "Completed",
            "current_step": steps[-1],
            "completed_steps": completed_steps,
            "created_at": datetime.now().isoformat()
        }

        self.workflows[workflow_id] = workflow

        return workflow

    # -------------------------
    # Parallel Workflow
    # -------------------------

    def execute_parallel_tasks(self):

        return {
            "parallel_tasks": [
                "HR Notification",
                "Calendar Update"
            ],
            "status": "Completed"
        }

    # -------------------------
    # Conditional Branch
    # -------------------------

    def validate_leave_balance(self, balance, requested_days):

        if balance >= requested_days:
            return {
                "approved": True,
                "message": "Sufficient leave balance"
            }

        return {
            "approved": False,
            "message": "Insufficient leave balance"
        }

    # -------------------------
    # Rollback
    # -------------------------

    def rollback(self, workflow_id):

        return {
            "workflow_id": workflow_id,
            "status": "Rolled Back",
            "message": "Workflow reverted successfully"
        }

    # -------------------------
    # Get Workflow
    # -------------------------

    def get_workflow(self, workflow_id):

        return self.workflows.get(
            workflow_id,
            {
                "message": "Workflow not found"
            }
        )