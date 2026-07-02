def authenticate():
    return True


def authorize(role: str):
    return role in ["Admin", "Payroll"]


def log_action(action: str):
    print(f"[PAYROLL TOOL LOG] {action}")


def generate_payroll(employee_id: str, role: str = "Admin"):
    if not authenticate():
        return {"status": "Failed", "message": "Authentication failed"}

    if not authorize(role):
        return {"status": "Failed", "message": "Unauthorized access"}

    log_action(f"Payroll generated for {employee_id}")

    return {
        "status": "Success",
        "employee_id": employee_id,
        "salary": 50000,
        "message": "Payroll generated successfully"
    }