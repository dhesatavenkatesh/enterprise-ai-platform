from fastapi import APIRouter
from pydantic import BaseModel
import uuid

router = APIRouter(
    prefix="/workflow",
    tags=["Enterprise Workflow APIs"]
)

workflows = {}


class WorkflowRequest(BaseModel):
    workflow_name: str
    requested_by: str


class WorkflowAction(BaseModel):
    workflow_id: str


@router.post("/start")
def start_workflow(request: WorkflowRequest):
    workflow_id = "WF-" + str(uuid.uuid4())[:8]

    workflow = {
        "workflow_id": workflow_id,
        "workflow_name": request.workflow_name,
        "requested_by": request.requested_by,
        "status": "Running",
        "current_step": "Manager Approval",
        "progress": "60%"
    }

    workflows[workflow_id] = workflow
    return workflow


@router.get("/history")
def workflow_history():
    return {
        "history": list(workflows.values())
    }


@router.get("/{workflow_id}")
def get_workflow(workflow_id: str):
    return workflows.get(
        workflow_id,
        {"message": "Workflow not found"}
    )


@router.post("/cancel")
def cancel_workflow(request: WorkflowAction):
    if request.workflow_id not in workflows:
        return {"message": "Workflow not found"}

    workflows[request.workflow_id]["status"] = "Cancelled"
    return workflows[request.workflow_id]


@router.post("/retry")
def retry_workflow(request: WorkflowAction):
    if request.workflow_id not in workflows:
        return {"message": "Workflow not found"}

    workflows[request.workflow_id]["status"] = "Running"
    return workflows[request.workflow_id]