from fastapi import Header, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from backend.authentication.jwt_handler import decode_token

# This enables Swagger Authorize button
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):

    token = credentials.credentials
    user = decode_token(token)

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    return user