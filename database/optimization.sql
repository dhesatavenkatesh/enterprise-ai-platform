
-- USERS TABLE INDEXES

DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name='users' AND column_name='email'
    ) THEN
        CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
    END IF;

    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name='users' AND column_name='username'
    ) THEN
        CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
    END IF;

    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name='users' AND column_name='role'
    ) THEN
        CREATE INDEX IF NOT EXISTS idx_users_role ON users(role);
    END IF;

    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name='users' AND column_name='tenant_id'
    ) THEN
        CREATE INDEX IF NOT EXISTS idx_users_tenant_id ON users(tenant_id);
    END IF;
END $$;


-- AUDIT LOGS TABLE INDEXES

DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name='audit_logs' AND column_name='user_id'
    ) THEN
        CREATE INDEX IF NOT EXISTS idx_audit_logs_user_id ON audit_logs(user_id);
    END IF;

    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name='audit_logs' AND column_name='endpoint'
    ) THEN
        CREATE INDEX IF NOT EXISTS idx_audit_logs_endpoint ON audit_logs(endpoint);
    END IF;

    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name='audit_logs' AND column_name='method'
    ) THEN
        CREATE INDEX IF NOT EXISTS idx_audit_logs_method ON audit_logs(method);
    END IF;

    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name='audit_logs' AND column_name='status_code'
    ) THEN
        CREATE INDEX IF NOT EXISTS idx_audit_logs_status_code ON audit_logs(status_code);
    END IF;

    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name='audit_logs' AND column_name='created_at'
    ) THEN
        CREATE INDEX IF NOT EXISTS idx_audit_logs_created_at ON audit_logs(created_at);
    END IF;

    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name='audit_logs' AND column_name='tenant_id'
    ) THEN
        CREATE INDEX IF NOT EXISTS idx_audit_logs_tenant_id ON audit_logs(tenant_id);
    END IF;
END $$;


-- DOCUMENTS TABLE INDEXES

DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.tables
        WHERE table_name='documents'
    ) THEN

        IF EXISTS (
            SELECT 1 FROM information_schema.columns
            WHERE table_name='documents' AND column_name='tenant_id'
        ) THEN
            CREATE INDEX IF NOT EXISTS idx_documents_tenant_id ON documents(tenant_id);
        END IF;

        IF EXISTS (
            SELECT 1 FROM information_schema.columns
            WHERE table_name='documents' AND column_name='namespace'
        ) THEN
            CREATE INDEX IF NOT EXISTS idx_documents_namespace ON documents(namespace);
        END IF;

        IF EXISTS (
            SELECT 1 FROM information_schema.columns
            WHERE table_name='documents' AND column_name='created_at'
        ) THEN
            CREATE INDEX IF NOT EXISTS idx_documents_created_at ON documents(created_at);
        END IF;

    END IF;
END $$;


-- PERMISSIONS TABLE INDEXES

DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.tables
        WHERE table_name='permissions'
    ) THEN

        IF EXISTS (
            SELECT 1 FROM information_schema.columns
            WHERE table_name='permissions' AND column_name='role'
        ) THEN
            CREATE INDEX IF NOT EXISTS idx_permissions_role ON permissions(role);
        END IF;

        IF EXISTS (
            SELECT 1 FROM information_schema.columns
            WHERE table_name='permissions' AND column_name='module'
        ) THEN
            CREATE INDEX IF NOT EXISTS idx_permissions_module ON permissions(module);
        END IF;

    END IF;
END $$;


-- ROLES TABLE INDEXES

DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.tables
        WHERE table_name='roles'
    ) THEN

        IF EXISTS (
            SELECT 1 FROM information_schema.columns
            WHERE table_name='roles' AND column_name='name'
        ) THEN
            CREATE INDEX IF NOT EXISTS idx_roles_name ON roles(name);
        END IF;

    END IF;
END $$;


-- SAFE DATABASE ANALYZE

DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name='users') THEN
        ANALYZE users;
    END IF;

    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name='audit_logs') THEN
        ANALYZE audit_logs;
    END IF;

    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name='roles') THEN
        ANALYZE roles;
    END IF;

    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name='permissions') THEN
        ANALYZE permissions;
    END IF;

    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name='documents') THEN
        ANALYZE documents;
    END IF;
END $$;


