import time


class MCPGateway:

    def __init__(self):

        self.tools = {
            "employee_service": {
                "version": "1.0",
                "status": "Healthy",
                "authenticated": True
            },

            "payroll_service": {
                "version": "1.0",
                "status": "Healthy",
                "authenticated": True
            },

            "leave_service": {
                "version": "1.0",
                "status": "Healthy",
                "authenticated": True
            },

            "project_service": {
                "version": "1.0",
                "status": "Healthy",
                "authenticated": True
            },

            "knowledge_base": {
                "version": "2.0",
                "status": "Healthy",
                "authenticated": True
            },

            "email_service": {
                "version": "1.2",
                "status": "Healthy",
                "authenticated": True
            },

            "calendar_service": {
                "version": "1.1",
                "status": "Healthy",
                "authenticated": True
            },

            "notification_service": {
                "version": "1.0",
                "status": "Healthy",
                "authenticated": True
            }
        }

    # -----------------------------
    # Tool Discovery
    # -----------------------------
    def discover_tools(self):
        return list(self.tools.keys())

    # -----------------------------
    # Health Check
    # -----------------------------
    def health_check(self):

        health = {}

        for tool, info in self.tools.items():
            health[tool] = info["status"]

        return health

    # -----------------------------
    # Authentication
    # -----------------------------
    def authenticate_tool(self, tool_name):

        tool = self.tools.get(tool_name)

        if tool is None:
            return False

        return tool["authenticated"]

    # -----------------------------
    # Version
    # -----------------------------
    def get_tool_version(self, tool_name):

        tool = self.tools.get(tool_name)

        if tool:
            return tool["version"]

        return None

    # -----------------------------
    # Retry Logic
    # -----------------------------
    def execute_tool(self, tool_name, retries=3):

        if tool_name not in self.tools:
            return {
                "status": "Failed",
                "message": "Tool not found"
            }

        for attempt in range(retries):

            try:

                time.sleep(0.2)

                return {
                    "status": "Success",
                    "tool": tool_name,
                    "attempt": attempt + 1,
                    "message": f"{tool_name} executed successfully"
                }

            except Exception:

                continue

        return {
            "status": "Failed",
            "tool": tool_name
        }