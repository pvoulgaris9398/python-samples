from __future__ import annotations

import structlog

from app.config import settings

try:
    from opentelemetry import trace
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor

    OTEL_AVAILABLE = True
except ImportError:  # pragma: no cover
    OTEL_AVAILABLE = False


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
        insecure=settings.otlp_insecure,
    )
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)

    FastAPIInstrumentor.instrument_app(app)
    SQLAlchemyInstrumentor().instrument(engine=engine)
