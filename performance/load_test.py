from locust import HttpUser, task, between


class EnterpriseAIUser(HttpUser):
    wait_time = between(1, 3)

    token = None

    def on_start(self):
        response = self.client.post(
            "/auth/login",
            json={
                "username": "admin",
                "password": "admin123"
            }
        )

        if response.status_code == 200:
            data = response.json()
            self.token = data.get("access_token")

    def auth_headers(self):
        if self.token:
            return {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            }

        return {
            "Content-Type": "application/json"
        }

    @task(3)
    def chat_api(self):
        self.client.post(
            "/chat",
            headers=self.auth_headers(),
            json={
                "message": "Explain company leave policy"
            }
        )

    @task(2)
    def rag_api(self):
        self.client.post(
            "/rag/search",
            headers=self.auth_headers(),
            json={
                "query": "HR leave policy",
                "top_k": 5
            }
        )

    @task(1)
    def workflow_api(self):
        self.client.post(
            "/workflow/run",
            headers=self.auth_headers(),
            json={
                "workflow_name": "leave_approval"
            }
        )

    @task(1)
    def agent_api(self):
        self.client.post(
            "/agent/run",
            headers=self.auth_headers(),
            json={
                "agent_name": "hr_agent",
                "task": "summarize HR policy"
            }
        )

    @task(2)
    def profile_api(self):
        self.client.get(
            "/auth/me",
            headers=self.auth_headers()
        )