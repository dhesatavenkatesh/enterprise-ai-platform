import json
import logging
from datetime import datetime


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "service": "blackroth-enterprise-ai-platform",
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        if hasattr(record, "user"):
            log_record["user"] = record.user

        if hasattr(record, "endpoint"):
            log_record["endpoint"] = record.endpoint

        if hasattr(record, "status_code"):
            log_record["status_code"] = record.status_code

        if hasattr(record, "event_type"):
            log_record["event_type"] = record.event_type

        return json.dumps(log_record)


logger = logging.getLogger("blackroth-json-logger")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())

if not logger.handlers:
    logger.addHandler(handler)


def log_event(message, level="info", **kwargs):
    extra = kwargs

    if level == "error":
        logger.error(message, extra=extra)
    elif level == "warning":
        logger.warning(message, extra=extra)
    else:
        logger.info(message, extra=extra)


class AlertManager:
    def __init__(self):
        self.alerts = []

    def create_alert(self, alert_type, severity, message):
        alert = {
            "timestamp": datetime.utcnow().isoformat(),
            "alert_type": alert_type,
            "severity": severity,
            "message": message,
            "channels": ["Grafana", "Slack", "Email"],
            "status": "Triggered"
        }

        self.alerts.append(alert)

        log_event(
            message="Alert triggered",
            level="warning",
            event_type=alert_type,
            status_code=500
        )

        return alert

    def check_high_error_rate(self, error_rate):
        if error_rate > 5:
            return self.create_alert(
                "High Error Rate",
                "Critical",
                f"Error rate is {error_rate}%"
            )

        return {"status": "Normal"}

    def check_slow_response(self, response_time):
        if response_time > 3:
            return self.create_alert(
                "Slow Response",
                "Warning",
                f"Average response time is {response_time} seconds"
            )

        return {"status": "Normal"}

    def check_high_cpu(self, cpu_usage):
        if cpu_usage > 80:
            return self.create_alert(
                "High CPU",
                "Critical",
                f"CPU usage is {cpu_usage}%"
            )

        return {"status": "Normal"}

    def check_high_memory(self, memory_usage):
        if memory_usage > 85:
            return self.create_alert(
                "High Memory",
                "Critical",
                f"Memory usage is {memory_usage}%"
            )

        return {"status": "Normal"}

    def check_failed_agent(self, agent_name):
        return self.create_alert(
            "Failed Agent",
            "Critical",
            f"{agent_name} failed during execution"
        )

    def check_failed_workflow(self, workflow_id):
        return self.create_alert(
            "Failed Workflow",
            "Critical",
            f"Workflow {workflow_id} failed"
        )

    def get_alerts(self):
        return self.alerts


alert_manager = AlertManager()