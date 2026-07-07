import time
import os
import psutil
import requests
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"

APIS = [
    {
        "name": "Authentication API",
        "method": "POST",
        "url": "/auth/login",
        "data": {
            "username": "admin",
            "password": "admin123"
        }
    },
    {
        "name": "Chat API",
        "method": "POST",
        "url": "/chat",
        "data": {
            "message": "Explain company leave policy"
        }
    },
    {
        "name": "RAG API",
        "method": "POST",
        "url": "/rag/search",
        "data": {
            "query": "HR leave policy"
        }
    },
    {
        "name": "Workflow API",
        "method": "POST",
        "url": "/workflow/run",
        "data": {
            "workflow_name": "leave_approval"
        }
    },
    {
        "name": "Agent API",
        "method": "POST",
        "url": "/agent/run",
        "data": {
            "agent_name": "hr_agent",
            "task": "summarize HR policy"
        }
    }
]


class APIProfiler:

    def __init__(self):
        self.results = []

    def estimate_tokens(self, text):
        if not text:
            return 0
        return len(str(text).split()) * 1.3

    def profile_api(self, api):
        full_url = BASE_URL + api["url"]

        process = psutil.Process(os.getpid())

        cpu_before = psutil.cpu_percent()
        memory_before = process.memory_info().rss / 1024 / 1024

        start_time = time.time()

        try:
            if api["method"] == "POST":
                response = requests.post(full_url, json=api["data"], timeout=10)
            else:
                response = requests.get(full_url, timeout=10)

            end_time = time.time()

            cpu_after = psutil.cpu_percent()
            memory_after = process.memory_info().rss / 1024 / 1024

            response_time = round((end_time - start_time) * 1000, 2)

            result = {
                "api": api["name"],
                "endpoint": api["url"],
                "status_code": response.status_code,
                "response_time_ms": response_time,
                "cpu_usage_percent": cpu_after - cpu_before,
                "memory_usage_mb": round(memory_after - memory_before, 2),
                "database_queries": "Estimated / check DB logs",
                "token_usage": round(self.estimate_tokens(api["data"]), 2),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

        except Exception as e:
            result = {
                "api": api["name"],
                "endpoint": api["url"],
                "status_code": "FAILED",
                "error": str(e),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

        self.results.append(result)

    def run_profiler(self):
        for api in APIS:
            print(f"Profiling {api['name']}...")
            self.profile_api(api)

    def generate_report(self):
        os.makedirs("docs", exist_ok=True)

        report_path = "docs/api_performance_report.md"

        with open(report_path, "w", encoding="utf-8") as file:
            file.write("# API Performance Report\n\n")
            file.write("## Sprint 7 – Performance Optimization\n\n")

            for result in self.results:
                file.write(f"### {result['api']}\n\n")
                for key, value in result.items():
                    file.write(f"- **{key}**: {value}\n")
                file.write("\n---\n\n")

            file.write("## Recommendations\n\n")
            file.write("- Add Redis caching for repeated requests.\n")
            file.write("- Optimize database queries using indexes.\n")
            file.write("- Reduce prompt length to reduce token usage.\n")
            file.write("- Use async processing for heavy AI workflows.\n")
            file.write("- Monitor latency, CPU, memory, and errors continuously.\n")

        print(f"Report generated: {report_path}")


if __name__ == "__main__":
    profiler = APIProfiler()
    profiler.run_profiler()
    profiler.generate_report()