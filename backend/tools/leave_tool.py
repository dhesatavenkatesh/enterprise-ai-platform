def authenticate():
    return True


def authorize(role: str):
    return role in ["Admin", "HR", "Manager", "Employee"]


def log_action(action: str):
    print(f"[LEAVE TOOL LOG] {action}")


def retry_operation(operation, retries=3):
    for attempt in range(retries):
        try:
            return operation()
        except Exception:
            continue
    return {"status": "Failed", "message": "Retry limit exceeded"}


def apply_leave(employee_id: str, days: int, role: str = "Employee"):
    if not authenticate():
        return {"status": "Failed", "message": "Authentication failed"}

    if not authorize(role):
        return {"status": "Failed", "message": "Unauthorized access"}

    if days <= 0:
        return {"status": "Failed", "message": "Invalid leave days"}

    def operation():
        log_action(f"Leave applied for {employee_id}")
        return {
            "status": "Success",
            "employee_id": employee_id,
            "leave_days": days,
            "message": "Leave application submitted"
        }

    return retry_operation(operation)