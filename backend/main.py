from fastapi import FastAPI, Request, Depends
from backend.audit.logger import log_request
from backend.auth.routes import router as auth_router
from backend.admin.routes import router as admin_router
from backend.auth.deps import get_current_user
from security.rbac import check_permission

app = FastAPI(
    title="Enterprise AI Platform",
    description="Enterprise AI Platform for BlackRoth",
    version="1.0.0"
)
@app.middleware("http")
async def audit_middleware(request: Request, call_next):
    response = await call_next(request)

    log_request(
        user="Unknown",
        ip=request.client.host,
        endpoint=request.url.path,
        method=request.method,
        status=response.status_code,
    )
    return response

app.include_router(auth_router)
app.include_router(admin_router)

@app.get(
    "/",
    summary="Application Status",
    description="Checks whether the Enterprise AI Platform is running."
)
def home():
    return {"status": "running"}

@app.get(
    "/hr/documents",
    summary="Access HR Documents",
    description="Allows HR users to access HR documents."
)
def hr_docs(user=Depends(get_current_user)):
    check_permission(user["role"], "hr_documents")
    return {"message": "HR Access Granted"}