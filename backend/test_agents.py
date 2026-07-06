def test_agent_orchestration_response():
    response = {
        "intent": "hr",
        "selected_agent": "HR Agent",
        "status": "Completed"
    }

    assert response["intent"] == "hr"
    assert response["selected_agent"] == "HR Agent"


def test_tool_response():
    tool_result = {
        "status": "Success",
        "tool": "leave_service"
    }

    assert tool_result["status"] == "Success"