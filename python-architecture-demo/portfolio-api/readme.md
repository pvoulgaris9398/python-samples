# Running

`cp .env.example .env`

`docker compose up --build`

- Open: `http://localhost:8000/health`
- Swagger: `http://localhost:8000/docs`

## OpenTelemetry Tracing

This sample can emit traces to an OTLP collector.

1. Copy the environment file:
   `cp .env.example .env`
2. Set `OTEL_ENABLED=true` in `.env`.
3. Ensure `OTLP_ENDPOINT` points to your collector, for example:
   `http://localhost:4318/v1/traces`
4. Build the image with OTEL dependencies included:
   `docker compose up --build`

The app uses `app.infrastructure.tracing.configure_tracing()` and the optional `otel` extras from `pyproject.toml`.

## Clean-Up

- Delete all build history in Docker Desktop:
  - `docker buildx history rm --all`

## Installing Dependencies

- Make sure `setuptools` is already installed in your `conda` environment
- Navigate to directory where `pyproject.toml` is and run:

`pip install -e .`

- Conda

## [structlog](https://www.structlog.org/en/stable/getting-started.html)