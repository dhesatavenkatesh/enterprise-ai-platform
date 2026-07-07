from dataclasses import dataclass


@dataclass
class TenantConfig:
    tenant_id: str
    tenant_name: str
    knowledge_base: str
    allowed_roles: list
    document_namespace: str


TENANTS = {
    "tenant_a": TenantConfig(
        tenant_id="tenant_a",
        tenant_name="Tenant A",
        knowledge_base="HR Documents",
        allowed_roles=["Admin", "HR", "Employee"],
        document_namespace="tenant_a_hr"
    ),
    "tenant_b": TenantConfig(
        tenant_id="tenant_b",
        tenant_name="Tenant B",
        knowledge_base="Engineering Documents",
        allowed_roles=["Admin", "Engineer", "Employee"],
        document_namespace="tenant_b_engineering"
    ),
    "tenant_c": TenantConfig(
        tenant_id="tenant_c",
        tenant_name="Tenant C",
        knowledge_base="Customer Support",
        allowed_roles=["Admin", "Support", "Employee"],
        document_namespace="tenant_c_support"
    )
}