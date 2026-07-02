from backend.agents.multi_agent import MultiAgentSystem

system = MultiAgentSystem()

result = system.collaborate(
    "Apply leave for 5 days and notify HR"
)

print(result)