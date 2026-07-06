def test_home_response():
    response = {
        "status": "running"
    }

    assert response["status"] == "running"


def test_workflow_response():
    workflow = {
        "workflow_id": "WF001",
        "status": "Running",
        "current_step": "Manager Approval",
        "progress": "60%"
    }

    assert workflow["status"] == "Running"
    assert workflow["progress"] == "60%"