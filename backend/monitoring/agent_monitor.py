from datetime import datetime
import random


class AgentMonitor:

    def __init__(self):

        self.monitor = {
            "active_agents": [],
            "running_tasks": [],
            "tool_usage": {},
            "workflow_success": 0,
            "workflow_failed": 0,
            "execution_times": [],
            "mcp_latency": [],
            "agent_cost": 0
        }

    # -------------------------
    # Active Agent
    # -------------------------

    def register_agent(self, agent_name):

        self.monitor["active_agents"].append({
            "agent": agent_name,
            "started": datetime.now().isoformat()
        })

    # -------------------------
    # Running Task
    # -------------------------

    def start_task(self, task_name):

        self.monitor["running_tasks"].append(task_name)

    def finish_task(self, task_name, success=True):

        if task_name in self.monitor["running_tasks"]:
            self.monitor["running_tasks"].remove(task_name)

        if success:
            self.monitor["workflow_success"] += 1
        else:
            self.monitor["workflow_failed"] += 1

    # -------------------------
    # Tool Usage
    # -------------------------

    def record_tool(self, tool_name):

        if tool_name not in self.monitor["tool_usage"]:
            self.monitor["tool_usage"][tool_name] = 0

        self.monitor["tool_usage"][tool_name] += 1

    # -------------------------
    # Execution Time
    # -------------------------

    def record_execution(self):

        self.monitor["execution_times"].append(
            round(random.uniform(0.2, 1.5), 2)
        )

    # -------------------------
    # MCP Latency
    # -------------------------

    def record_latency(self):

        self.monitor["mcp_latency"].append(
            round(random.uniform(20, 150), 2)
        )

    # -------------------------
    # Agent Cost
    # -------------------------

    def record_cost(self, cost):

        self.monitor["agent_cost"] += cost

    # -------------------------
    # Dashboard
    # -------------------------

    def dashboard(self):

        avg_time = 0

        if self.monitor["execution_times"]:
            avg_time = round(
                sum(self.monitor["execution_times"])
                / len(self.monitor["execution_times"]),
                2
            )

        avg_latency = 0

        if self.monitor["mcp_latency"]:
            avg_latency = round(
                sum(self.monitor["mcp_latency"])
                / len(self.monitor["mcp_latency"]),
                2
            )

        return {

            "Active Agents":
                len(self.monitor["active_agents"]),

            "Running Tasks":
                len(self.monitor["running_tasks"]),

            "Tool Usage":
                self.monitor["tool_usage"],

            "Workflow Success":
                self.monitor["workflow_success"],

            "Failed Executions":
                self.monitor["workflow_failed"],

            "Average Execution Time":
                f"{avg_time} sec",

            "Average MCP Latency":
                f"{avg_latency} ms",

            "Agent Cost":
                f"${self.monitor['agent_cost']:.2f}"
        }