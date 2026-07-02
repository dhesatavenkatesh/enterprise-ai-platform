def authenticate():
    return True


def authorize(role: str):
    return role in ["Admin", "Manager", "Employee"]


def log_action(action: str):
    print(f"[PROJECT TOOL LOG] {action}")


def get_project_status(project_id: str, role: str = "Manager"):
    if not authenticate():
        return {"status": "Failed", "message": "Authentication failed"}

    if not authorize(role):
        return {"status": "Failed", "message": "Unauthorized access"}

    log_action(f"Fetched project status {project_id}")

    return {
        "status": "Success",
        "project_id": project_id,
        "project_status": "In Progress",
        "completion": "65%"
    }