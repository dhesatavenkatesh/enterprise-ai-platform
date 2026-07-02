from backend.monitoring.agent_monitor import AgentMonitor

monitor = AgentMonitor()

monitor.register_agent("HR Agent")
monitor.register_agent("Planner Agent")
monitor.register_agent("Knowledge Agent")

monitor.start_task("Leave Workflow")
monitor.record_tool("Leave Service")
monitor.record_tool("Knowledge Base")
monitor.record_tool("Knowledge Base")

monitor.record_execution()
monitor.record_execution()

monitor.record_latency()
monitor.record_latency()

monitor.record_cost(0.15)
monitor.record_cost(0.22)

monitor.finish_task("Leave Workflow")

print(monitor.dashboard())