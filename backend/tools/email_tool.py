def authenticate():
    return True


def authorize(role: str):
    return role in ["Admin", "HR", "Manager"]


def log_action(action: str):
    print(f"[EMAIL TOOL LOG] {action}")


def send_email(to: str, subject: str, body: str, role: str = "Admin"):
    if not authenticate():
        return {"status": "Failed", "message": "Authentication failed"}

    if not authorize(role):
        return {"status": "Failed", "message": "Unauthorized access"}

    if "@" not in to:
        return {"status": "Failed", "message": "Invalid email address"}

    log_action(f"Email sent to {to}")

    return {
        "status": "Success",
        "to": to,
        "subject": subject,
        "message": "Email sent successfully"
    }