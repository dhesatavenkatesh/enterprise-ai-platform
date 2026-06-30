from fastapi import APIRouter
from pydantic import BaseModel
from backend.authentication.password_handler import verify_password
from backend.authentication.jwt_handler import create_access_token

router = APIRouter()
class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(user: LoginRequest):
    # Demo user (later this will come from PostgreSQL)
    demo_email = "admin@gmail.com"
    demo_password_hash = "$2b$12$Ne2tDG4.KBFPjPXiapEOv.urdXitv.OWzxhlxY9MzrBXvBxcbjqdy"

    if user.email != demo_email:
        return {"message": "Invalid email"}

    if not verify_password(user.password, demo_password_hash):
        return {"message": "Invalid password"}

    token = create_access_token(
        {
            "sub": user.email,
            "role": "Admin"
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
@router.post("/logout")
def logout():
    return {
        "message": "Logged out successfully"
    }
@router.post("/refresh-token")
def refresh_token():
    token = create_access_token(
        {
            "sub": "admin@gmail.com",
            "role": "Admin"
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }