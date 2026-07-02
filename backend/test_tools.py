from backend.tools.employee_tool import get_employee
from backend.tools.leave_tool import apply_leave
from backend.tools.payroll_tool import generate_payroll
from backend.tools.project_tool import get_project_status
from backend.tools.email_tool import send_email
from backend.tools.calendar_tool import schedule_meeting
from backend.tools.notification_tool import send_notification

print(get_employee("EMP101", role="Admin"))
print(apply_leave("EMP101", 5, role="Employee"))
print(generate_payroll("EMP101", role="Admin"))
print(get_project_status("PRJ001", role="Manager"))
print(send_email("hr@company.com", "Leave Request", "Please approve leave", role="Manager"))
print(schedule_meeting("Sprint Review", "2026-07-01", role="Employee"))
print(send_notification("EMP101", "Your leave request is pending approval", role="Admin"))