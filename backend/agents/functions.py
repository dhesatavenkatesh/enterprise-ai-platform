def get_employee(employee_id):
    return {
        "employee_id": employee_id,
        "name": "John Doe",
        "department": "HR"
    }


def apply_leave(employee_id, days):
    return {
        "employee_id": employee_id,
        "leave_days": days,
        "status": "Leave Applied"
    }


def cancel_leave(employee_id):
    return {
        "employee_id": employee_id,
        "status": "Leave Cancelled"
    }


def generate_payroll(employee_id):
    return {
        "employee_id": employee_id,
        "salary": 50000
    }


def get_project_status(project_id):
    return {
        "project_id": project_id,
        "status": "In Progress"
    }


def search_documents(query):
    return {
        "query": query,
        "documents_found": 5
    }


def schedule_meeting(title):
    return {
        "meeting": title,
        "status": "Scheduled"
    }


def send_email(to):
    return {
        "recipient": to,
        "status": "Email Sent"
    }