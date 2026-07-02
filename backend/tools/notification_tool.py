def authenticate():
    return True


def authorize(role: str):
    return role in ["Admin", "HR", "Manager", "Employee"]


def log_action(action: str):
    print(f"[NOTIFICATION TOOL LOG] {action}")


def send_notification(user_id: str, message: str, role: str = "Admin"):
    if not authenticate():
        return {"status": "Failed", "message": "Authentication failed"}

    if not authorize(role):
        return {"status": "Failed", "message": "Unauthorized access"}

    log_action(f"Notification sent to {user_id}")

    return {
        "status": "Success",
        "user_id": user_id,
        "message": message
    }