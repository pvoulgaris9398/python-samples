from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "portfolio-api"

    postgres_host: str
    postgres_port: int

    postgres_db: str
    postgres_user: str
    postgres_password: str

    log_level: str = "INFO"

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


settings = Settings()
