from fastapi import APIRouter, Header, HTTPException
from backend.multitenancy.tenant_manager import TenantManager


router = APIRouter(
    prefix="/tenants",
    tags=["Multi-Tenancy"]
)

tenant_manager = TenantManager()


@router.get("/config")
def get_tenant_config(x_tenant_id: str = Header(...)):
    try:
        return tenant_manager.get_tenant_config(x_tenant_id)
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))


@router.get("/knowledge-base")
def get_knowledge_base(x_tenant_id: str = Header(...)):
    try:
        kb = tenant_manager.get_tenant_knowledge_base(x_tenant_id)

        return {
            "tenant_id": x_tenant_id,
            "knowledge_base": kb
        }

    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))


@router.get("/documents/{document_namespace}")
def access_tenant_document(
    document_namespace: str,
    x_tenant_id: str = Header(...)
):
    try:
        tenant_manager.check_document_access(
            x_tenant_id,
            document_namespace
        )

        return {
            "message": "Document access granted",
            "tenant_id": x_tenant_id,
            "document_namespace": document_namespace
        }

    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))


@router.post("/audit")
def tenant_audit_log(
    user: str,
    action: str,
    status: str,
    x_tenant_id: str = Header(...)
):
    try:
        log = tenant_manager.create_tenant_audit_log(
            x_tenant_id,
            user,
            action,
            status
        )

        return log

    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))