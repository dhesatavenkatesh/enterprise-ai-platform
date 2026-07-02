def authenticate():
    return True


def authorize(role: str):
    return role in ["Admin", "HR", "Manager"]


def log_action(action: str):
    print(f"[EMPLOYEE TOOL LOG] {action}")


def get_employee(employee_id: str, role: str = "Admin"):
    if not authenticate():
        return {"status": "Failed", "message": "Authentication failed"}

    if not authorize(role):
        return {"status": "Failed", "message": "Unauthorized access"}

    if not employee_id:
        return {"status": "Failed", "message": "Invalid employee ID"}

    log_action(f"Fetched employee {employee_id}")

    return {
        "status": "Success",
        "employee": {
            "employee_id": employee_id,
            "name": "John Doe",
            "department": "HR",
            "role": "Employee"
        }
    }