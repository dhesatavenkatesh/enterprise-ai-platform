import uuid
from datetime import datetime, timedelta


class ApprovalEngine:

    def __init__(self):
        self.pending_queue = {}
        self.approval_history = []
        self.audit_trail = []

    def create_approval(self, approval_type, requested_by, details):
        approval_id = "APR-" + str(uuid.uuid4())[:8]

        approval = {
            "approval_id": approval_id,
            "approval_type": approval_type,
            "requested_by": requested_by,
            "details": details,
            "status": "Pending",
            "created_at": datetime.now().isoformat(),
            "due_date": (datetime.now() + timedelta(days=2)).isoformat()
        }

        self.pending_queue[approval_id] = approval
        self.audit_trail.append({
            "action": "Approval Created",
            "approval_id": approval_id,
            "timestamp": datetime.now().isoformat()
        })

        return approval

    def approve(self, approval_id, approved_by):
        if approval_id not in self.pending_queue:
            return {"error": "Approval request not found"}

        approval = self.pending_queue.pop(approval_id)
        approval["status"] = "Approved"
        approval["approved_by"] = approved_by
        approval["approved_at"] = datetime.now().isoformat()

        self.approval_history.append(approval)
        self.audit_trail.append({
            "action": "Approved",
            "approval_id": approval_id,
            "approved_by": approved_by,
            "timestamp": datetime.now().isoformat()
        })

        return approval

    def reject(self, approval_id, rejected_by, reason):
        if approval_id not in self.pending_queue:
            return {"error": "Approval request not found"}

        approval = self.pending_queue.pop(approval_id)
        approval["status"] = "Rejected"
        approval["rejected_by"] = rejected_by
        approval["reason"] = reason
        approval["rejected_at"] = datetime.now().isoformat()

        self.approval_history.append(approval)
        self.audit_trail.append({
            "action": "Rejected",
            "approval_id": approval_id,
            "rejected_by": rejected_by,
            "timestamp": datetime.now().isoformat()
        })

        return approval

    def get_pending_queue(self):
        return list(self.pending_queue.values())

    def get_approval_history(self):
        return self.approval_history

    def send_reminders(self):
        reminders = []

        for approval_id, approval in self.pending_queue.items():
            reminders.append({
                "approval_id": approval_id,
                "message": "Reminder sent to approver"
            })

        return reminders

    def escalate_overdue(self):
        now = datetime.now()
        escalated = []

        for approval_id, approval in self.pending_queue.items():
            due_date = datetime.fromisoformat(approval["due_date"])

            if now > due_date:
                approval["status"] = "Escalated"
                escalated.append(approval)

        return escalated

    def get_audit_trail(self):
        return self.audit_trail