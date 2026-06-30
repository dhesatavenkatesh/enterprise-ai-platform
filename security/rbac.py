from fastapi import HTTPException

ROLE_PERMISSIONS = {
    "HR": ["leave_policies", "onboarding", "hr_documents"],
    "Employee": ["chat"],
    "Admin": ["*"]
}

def check_permission(role: str, module: str):

    if role == "Admin":
        return True

    allowed = ROLE_PERMISSIONS.get(role, [])

    if module not in allowed:
        raise HTTPException(status_code=403, detail="Access Denied")

    return True