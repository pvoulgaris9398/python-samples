from pydantic import BaseModel


class HealthMetrics(BaseModel):
    uptime_seconds: float
    database_query_success: bool


class HealthTrace(BaseModel):
    trace_id: str | None = None
    span_id: str | None = None
    otel_enabled: bool


class HealthLogs(BaseModel):
    configured: bool
    log_level: str


class HealthResponse(BaseModel):
    status: str
    database: bool
    metrics: HealthMetrics
    trace: HealthTrace
    logs: HealthLogs
