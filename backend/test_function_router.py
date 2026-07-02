from backend.agents.function_router import FunctionRouter

from backend.agents.functions import (
    get_employee,
    apply_leave,
    cancel_leave,
    generate_payroll,
    get_project_status,
    search_documents,
    schedule_meeting,
    send_email
)

router = FunctionRouter()

router.register("get_employee", get_employee)
router.register("apply_leave", apply_leave)
router.register("cancel_leave", cancel_leave)
router.register("generate_payroll", generate_payroll)
router.register("get_project_status", get_project_status)
router.register("search_documents", search_documents)
router.register("schedule_meeting", schedule_meeting)
router.register("send_email", send_email)

print(router.execute("get_employee", employee_id="EMP101"))

print(router.execute("apply_leave", employee_id="EMP101", days=5))

print(router.execute("generate_payroll", employee_id="EMP101"))

print(router.execute("search_documents", query="Leave Policy"))

print(router.execute("schedule_meeting", title="Sprint Review"))

print(router.execute("send_email", to="hr@company.com"))