def authenticate():
    return True


def authorize(role: str):
    return role in ["Admin", "HR", "Manager", "Employee"]


def log_action(action: str):
    print(f"[CALENDAR TOOL LOG] {action}")


def schedule_meeting(title: str, date: str, role: str = "Employee"):
    if not authenticate():
        return {"status": "Failed", "message": "Authentication failed"}

    if not authorize(role):
        return {"status": "Failed", "message": "Unauthorized access"}

    log_action(f"Meeting scheduled: {title}")

    return {
        "status": "Success",
        "title": title,
        "date": date,
        "message": "Meeting scheduled successfully"
    }