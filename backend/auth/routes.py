from fastapi import APIRouter
from backend.authentication.jwt_handler import create_access_token

router = APIRouter()

@router.post("/login")
def login():
    user = {
        "id": 1,
        "name": "Kavya",
        "role": "HR"
    }

    token = create_access_token(user)

    return {"access_token": token, "token_type": "bearer"}