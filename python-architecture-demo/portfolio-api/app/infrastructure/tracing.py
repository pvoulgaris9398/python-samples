from __future__ import annotations

import structlog

from app.config import settings

try:
    import opentelemetry.instrumentation.fastapi
    import opentelemetry.instrumentation.sqlalchemy
    from opentelemetry import trace
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor

    OTEL_AVAILABLE = True
except ImportError:  # pragma: no cover
    trace = None
    OTEL_AVAILABLE = False


def get_trace_ids() -> tuple[str | None, str | None]:
    if not OTEL_AVAILABLE or trace is None:
        return None, None

    span = trace.get_current_span()
    if not span:
        return None, None

    span_context = span.get_span_context()
    if not span_context.is_valid:
        return None, None

    return (
        format(span_context.trace_id, "032x"),
        format(span_context.span_id, "016x"),
    )


def configure_tracing(app, engine):
    logger = structlog.get_logger()

    if not settings.otel_enabled:
        logger.info("otel.tracing.disabled", reason="disabled_in_settings")
        return

    if not OTEL_AVAILABLE:
        logger.warning("otel.tracing.disabled", reason="missing_dependency")
        return

    resource = Resource.create({"service.name": settings.app_name})
    provider = TracerProvider(resource=resource)
    exporter = OTLPSpanExporter(
        endpoint=settings.otlp_endpoint,
        # insecure=settings.otlp_insecure,
    )
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)

    opentelemetry.instrumentation.fastapi.FastAPIInstrumentor.instrument_app(app)
    opentelemetry.instrumentation.sqlalchemy.SQLAlchemyInstrumentor().instrument(
        engine=engine.sync_engine
    )
