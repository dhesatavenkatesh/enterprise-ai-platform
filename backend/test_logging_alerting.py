from backend.monitoring.logging import log_event, alert_manager

log_event(
    message="User accessed AI Chat",
    level="info",
    user="EMP101",
    endpoint="/chat",
    status_code=200,
    event_type="User Action"
)

print(alert_manager.check_high_error_rate(7))
print(alert_manager.check_slow_response(4.2))
print(alert_manager.check_high_cpu(85))
print(alert_manager.check_high_memory(90))
print(alert_manager.check_failed_agent("HR Agent"))
print(alert_manager.check_failed_workflow("WF001"))

print(alert_manager.get_alerts())