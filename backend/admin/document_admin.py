from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/admin/documents",
    tags=["Document Administration"]
)

documents = {
    1: {
        "id": 1,
        "title": "Leave Policy",
        "status": "Pending",
        "version": 1
    },
    2: {
        "id": 2,
        "title": "Payroll Guide",
        "status": "Pending",
        "version": 1
    }
}

audit_logs = []

version_history = {
    1: [
        {"version": 1, "title": "Leave Policy", "status": "Pending"}
    ],
    2: [
        {"version": 1, "title": "Payroll Guide", "status": "Pending"}
    ]
}


class RestoreRequest(BaseModel):
    version: int


class BulkDeleteRequest(BaseModel):
    document_ids: List[int]


def add_audit_log(action: str, document_id: int):
    audit_logs.append({
        "action": action,
        "document_id": document_id
    })


@router.post("/{document_id}/approve")
def approve_document(document_id: int):
    if document_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")

    documents[document_id]["status"] = "Approved"
    add_audit_log("Approved document", document_id)

    return {
        "message": "Document approved successfully",
        "document": documents[document_id]
    }


@router.post("/{document_id}/reject")
def reject_document(document_id: int):
    if document_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")

    documents[document_id]["status"] = "Rejected"
    add_audit_log("Rejected document", document_id)

    return {
        "message": "Document rejected successfully",
        "document": documents[document_id]
    }


@router.post("/{document_id}/archive")
def archive_document(document_id: int):
    if document_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")

    documents[document_id]["status"] = "Archived"
    add_audit_log("Archived document", document_id)

    return {
        "message": "Document archived successfully",
        "document": documents[document_id]
    }


@router.get("/{document_id}/versions")
def get_version_history(document_id: int):
    if document_id not in version_history:
        raise HTTPException(status_code=404, detail="Version history not found")

    return {
        "document_id": document_id,
        "versions": version_history[document_id]
    }


@router.post("/{document_id}/restore")
def restore_version(document_id: int, request: RestoreRequest):
    if document_id not in version_history:
        raise HTTPException(status_code=404, detail="Version history not found")

    for version in version_history[document_id]:
        if version["version"] == request.version:
            documents[document_id] = {
                "id": document_id,
                "title": version["title"],
                "status": version["status"],
                "version": version["version"]
            }

            add_audit_log("Restored document version", document_id)

            return {
                "message": "Document version restored",
                "document": documents[document_id]
            }

    raise HTTPException(status_code=404, detail="Version not found")


@router.delete("/bulk-delete")
def bulk_delete_documents(request: BulkDeleteRequest):
    deleted = []

    for document_id in request.document_ids:
        if document_id in documents:
            del documents[document_id]
            deleted.append(document_id)
            add_audit_log("Bulk deleted document", document_id)

    return {
        "message": "Bulk delete completed",
        "deleted_documents": deleted
    }


@router.get("/audit/logs")
def get_audit_logs():
    return {
        "audit_logs": audit_logs
    }
