from fastapi import APIRouter
from security.jwt_handler import create_token

router = APIRouter()

@router.post("/login")
def login():
    user = {
        "id": 1,
        "name": "Kavya",
        "role": "HR"
    }

    token = create_token(user)

    return {"access_token": token, "token_type": "bearer"}