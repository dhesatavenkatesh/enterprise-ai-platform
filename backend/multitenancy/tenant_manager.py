from datetime import datetime
from backend.multitenancy.tenant_config import TENANTS


class TenantManager:

    def identify_tenant(self, tenant_id):
        if tenant_id not in TENANTS:
            raise Exception("Invalid tenant ID")

        return TENANTS[tenant_id]

    def check_tenant_role(self, tenant_id, role):
        tenant = self.identify_tenant(tenant_id)

        if role not in tenant.allowed_roles:
            raise Exception("Role not allowed for this tenant")

        return True

    def get_tenant_knowledge_base(self, tenant_id):
        tenant = self.identify_tenant(tenant_id)
        return tenant.knowledge_base

    def check_document_access(self, tenant_id, document_namespace):
        tenant = self.identify_tenant(tenant_id)

        if tenant.document_namespace != document_namespace:
            raise Exception("Access denied: cross-tenant data access blocked")

        return True

    def get_tenant_config(self, tenant_id):
        tenant = self.identify_tenant(tenant_id)

        return {
            "tenant_id": tenant.tenant_id,
            "tenant_name": tenant.tenant_name,
            "knowledge_base": tenant.knowledge_base,
            "allowed_roles": tenant.allowed_roles,
            "document_namespace": tenant.document_namespace
        }

    def create_tenant_audit_log(self, tenant_id, user, action, status):
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tenant_id": tenant_id,
            "user": user,
            "action": action,
            "status": status
        }