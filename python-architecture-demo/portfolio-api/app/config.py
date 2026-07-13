from typing import Any

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "portfolio-api"

    def __init__(self, **values: Any) -> None:
        super().__init__(**values)

    postgres_host: str
    postgres_port: int

    postgres_db: str
    postgres_user: str
    postgres_password: str

    log_level: str = "INFO"
    otel_enabled: bool = False
    otlp_endpoint: str = "http://localhost:4318/v1/traces"
    otlp_insecure: bool = True

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.postgres_user}:"
            f"{self.postgres_password}@"
            f"{self.postgres_host}:"
            f"{self.postgres_port}/"
            f"{self.postgres_db}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
