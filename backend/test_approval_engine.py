from backend.workflows.approval_engine import ApprovalEngine

engine = ApprovalEngine()

approval = engine.create_approval(
    approval_type="Leave Approval",
    requested_by="EMP101",
    details={
        "leave_days": 5,
        "reason": "Family function"
    }
)

print("\nCreated Approval")
print(approval)

approval_id = approval["approval_id"]

print("\nPending Queue")
print(engine.get_pending_queue())

print("\nApprove Request")
print(engine.approve(approval_id, approved_by="MANAGER001"))

print("\nApproval History")
print(engine.get_approval_history())

print("\nAudit Trail")
print(engine.get_audit_trail())

print("\nReminders")
print(engine.send_reminders())
