from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor


def setup_tracing(app):
    resource = Resource.create({
        "service.name": "blackroth-enterprise-ai-platform"
    })

    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    console_exporter = ConsoleSpanExporter()
    span_processor = BatchSpanProcessor(console_exporter)

    provider.add_span_processor(span_processor)

    FastAPIInstrumentor.instrument_app(app)

    return trace.get_tracer("blackroth-tracer")


tracer = trace.get_tracer("blackroth-tracer")


def trace_rag_pipeline(query: str):
    with tracer.start_as_current_span("rag_pipeline") as span:
        span.set_attribute("query", query)

        with tracer.start_as_current_span("gateway"):
            pass

        with tracer.start_as_current_span("rag_retrieval"):
            pass

        with tracer.start_as_current_span("llm_generation"):
            pass

        with tracer.start_as_current_span("agent_execution"):
            pass

        with tracer.start_as_current_span("database_access"):
            pass

        return {
            "status": "trace_completed",
            "query": query
        }