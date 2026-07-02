from backend.agents.agent_orchestrator import AgentOrchestrator

orchestrator = AgentOrchestrator()

result = orchestrator.orchestrate(
    "I want to apply leave for next week"
)

print(result)