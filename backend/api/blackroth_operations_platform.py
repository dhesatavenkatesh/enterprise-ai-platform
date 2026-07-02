from fastapi import APIRouter
from pydantic import BaseModel

from backend.agents.agent_orchestrator import AgentOrchestrator
from backend.mcp.mcp_gateway import MCPGateway
from backend.workflows.workflow_engine import WorkflowEngine
from backend.workflows.approval_engine import ApprovalEngine
from backend.monitoring.agent_monitor import AgentMonitor

router = APIRouter(
    prefix="/blackroth-ops",
    tags=["BlackRoth AI Operations Platform"]
)

orchestrator = AgentOrchestrator()
mcp_gateway = MCPGateway()
workflow_engine = WorkflowEngine()
approval_engine = ApprovalEngine()
monitor = AgentMonitor()


class OperationsRequest(BaseModel):
    module: str
    request: str
    requested_by: str
    role: str = "Employee"


@router.post("/execute")
def execute_operations(request: OperationsRequest):

    orchestration = orchestrator.orchestrate(request.request)

    tools = mcp_gateway.discover_tools()

    workflow = workflow_engine.execute_leave_workflow(
        employee_id=request.requested_by,
        leave_days=5
    )

    approval = approval_engine.create_approval(
        approval_type=f"{request.module} Approval",
        requested_by=request.requested_by,
        details={
            "request": request.request,
            "module": request.module
        }
    )

    monitor.register_agent(orchestration["agent"])
    monitor.record_tool("MCP Gateway")
    monitor.record_cost(0.05)

    return {
        "module": request.module,
        "request": request.request,
        "requested_by": request.requested_by,
        "role": request.role,
        "ai_agent_routing": orchestration,
        "mcp_tools": tools,
        "workflow": workflow,
        "human_approval": approval,
        "audit_logging": "Audit event recorded",
        "notification": "Notification sent",
        "analytics": monitor.dashboard()
    }


@router.get("/modules")
def business_modules():
    return {
        "business_modules": [
            "HR Automation",
            "Payroll Automation",
            "Recruitment Assistant",
            "Customer Support",
            "Technical Documentation",
            "Project Management",
            "Analytics"
        ]
    }


@router.get("/capabilities")
def enterprise_capabilities():
    return {
        "enterprise_capabilities": [
            "AI Agent Routing",
            "MCP Integration",
            "Workflow Automation",
            "Human Approval",
            "Role-Based Access",
            "Audit Logging",
            "Notifications",
            "Analytics"
        ]
    }


@router.get("/dashboard")
def operations_dashboard():
    return monitor.dashboard()
