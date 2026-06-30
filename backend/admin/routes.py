from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["Admin Dashboard"]
)

USERS = []

@router.get(
    "/users",
    summary="Get All Users",
    description="Returns a list of all users."
)
def get_users():
    return USERS

@router.post(
    "/users",
    summary="Create User",
    description="Creates a new user."
)
def create_user(user: dict):
    USERS.append(user)
    return {
        "message": "User created",
        "user": user
    }

@router.post(
    "/users",
    summary="Create User",
    description="Creates a new user."
)
def update_user(user_id: int, updated_user: dict):
    if user_id < len(USERS):
        USERS[user_id] = updated_user
        return {"message": "User updated"}
    return {"message": "User not found"}

@router.delete(
    "/users/{user_id}",
    summary="Delete User",
    description="Deletes a user by their ID."
)
def delete_user(user_id: int):
    if user_id < len(USERS):
        USERS.pop(user_id)
        return {"message": "User deleted"}
    return {"message": "User not found"}

@router.get(
    "/roles",
    summary="Get Roles",
    description="Returns a list of all available roles."
)
def get_roles():
    return [
        "Admin",
        "HR",
        "Manager",
        "Employee",
        "Support"
    ]

@router.get(
    "/permissions",
    summary="Get Permissions",
    description="Returns a list of all available permissions."
)
def get_permissions():
    return {
        "HR": [
            "leave_policies",
            "onboarding",
            "hr_documents"
        ],
        "Employee": [
            "chat"
        ],
        "Admin": [
            "*"
        ]
    }