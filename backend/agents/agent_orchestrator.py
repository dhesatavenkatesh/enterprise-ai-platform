import uuid
from datetime import datetime


class AgentOrchestrator:

    def __init__(self):
        self.supported_agents = {
            "hr": "HR Agent",
            "payroll": "Payroll Agent",
            "knowledge": "Knowledge Agent",
            "project": "Project Management Agent",
            "analytics": "Analytics Agent",
            "support": "Customer Support Agent"
        }

        self.intent_keywords = {
            "hr": ["leave", "policy", "onboarding", "employee"],
            "payroll": ["salary", "payroll", "payslip", "compensation"],
            "knowledge": ["document", "search", "knowledge", "file"],
            "project": ["project", "task", "status", "deadline"],
            "analytics": ["report", "analytics", "metrics", "dashboard"],
            "support": ["issue", "ticket", "support", "help"]
        }

    def detect_intent(self, request: str):
        request_lower = request.lower()

        for intent, keywords in self.intent_keywords.items():
            for keyword in keywords:
                if keyword in request_lower:
                    return intent

        return "knowledge"

    def route_agent(self, intent: str):
        return self.supported_agents.get(intent, "Knowledge Agent")

    def plan_workflow(self, intent: str, request: str):
        workflow_id = "WF-" + str(uuid.uuid4())[:8]

        steps = [
            "Validate user request",
            f"Route to {self.route_agent(intent)}",
            "Select required enterprise tools",
            "Execute workflow steps",
            "Validate output",
            "Return response"
        ]

        return {
            "workflow_id": workflow_id,
            "intent": intent,
            "request": request,
            "steps": steps,
            "created_at": datetime.now().isoformat()
        }

    def select_tools(self, intent: str):
        tool_map = {
            "hr": ["Employee Service", "Leave Service", "Notification Service"],
            "payroll": ["Payroll Service", "Employee Service"],
            "knowledge": ["Knowledge Base"],
            "project": ["Project Service", "Calendar Service"],
            "analytics": ["Analytics Service"],
            "support": ["Customer Support Service", "Notification Service"]
        }

        return tool_map.get(intent, ["Knowledge Base"])

    def aggregate_results(self, workflow: dict, tools: list):
        return {
            "workflow_id": workflow["workflow_id"],
            "intent": workflow["intent"],
            "agent": self.route_agent(workflow["intent"]),
            "tools": tools,
            "steps": workflow["steps"],
            "status": "Completed",
            "message": "Agent orchestration completed successfully"
        }

    def recover_from_error(self, error: str):
        return {
            "status": "Recovered",
            "error": error,
            "action": "Fallback to Knowledge Agent"
        }

    def orchestrate(self, request: str):
        try:
            intent = self.detect_intent(request)
            agent = self.route_agent(intent)
            workflow = self.plan_workflow(intent, request)
            tools = self.select_tools(intent)
            result = self.aggregate_results(workflow, tools)

            result["selected_agent"] = agent

            return result

        except Exception as error:
            return self.recover_from_error(str(error))