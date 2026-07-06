import time

from fastapi import APIRouter, Request, Response
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    Counter,
    Gauge,
    Histogram,
    generate_latest,
)

router = APIRouter(tags=["Monitoring"])


# -----------------------------
# Application Metrics
# -----------------------------

REQUEST_COUNT = Counter(
    "blackroth_http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status_code"],
)

RESPONSE_TIME = Histogram(
    "blackroth_http_response_time_seconds",
    "HTTP request response time in seconds",
    ["method", "endpoint"],
)

ERROR_COUNT = Counter(
    "blackroth_http_errors_total",
    "Total number of HTTP errors",
    ["method", "endpoint", "status_code"],
)

ACTIVE_USERS = Gauge(
    "blackroth_active_users",
    "Current number of active users",
)


# -----------------------------
# AI Metrics
# -----------------------------

TOKEN_USAGE = Counter(
    "blackroth_ai_tokens_total",
    "Total number of AI tokens used",
    ["model", "token_type"],
)

RAG_RETRIEVAL_TIME = Histogram(
    "blackroth_rag_retrieval_seconds",
    "RAG retrieval processing time",
)

AGENT_EXECUTION_TIME = Histogram(
    "blackroth_agent_execution_seconds",
    "AI agent execution time",
    ["agent_name"],
)

TOOL_CALLS = Counter(
    "blackroth_tool_calls_total",
    "Total number of AI tool calls",
    ["tool_name", "status"],
)


# -----------------------------
# Metrics Middleware
# -----------------------------

async def metrics_middleware(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    duration = time.perf_counter() - start_time

    endpoint = request.url.path
    method = request.method
    status_code = str(response.status_code)

    REQUEST_COUNT.labels(
        method=method,
        endpoint=endpoint,
        status_code=status_code,
    ).inc()

    RESPONSE_TIME.labels(
        method=method,
        endpoint=endpoint,
    ).observe(duration)

    if response.status_code >= 400:
        ERROR_COUNT.labels(
            method=method,
            endpoint=endpoint,
            status_code=status_code,
        ).inc()

    return response


# -----------------------------
# Prometheus Endpoint
# -----------------------------

@router.get("/metrics", include_in_schema=True)
async def get_metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )