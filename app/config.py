from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Configuración central del servicio.
    Lee desde variables de entorno y/o archivo .env.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # App
    app_name: str = Field(default="rag-service")
    env: str = Field(default="dev")  # dev|staging|prod
    log_level: str = Field(default="INFO")

    # API
    api_prefix: str = Field(default="/v1")
    cors_origins: str = Field(default="*")  # csv: "http://localhost,http://127.0.0.1"

    # Multi-tenant (cómo se identifica el tenant)
    tenant_header: str = Field(default="X-Tenant-Id")

    # DB (más adelante)
    database_url: str = Field(default="postgresql+psycopg://postgres:postgres@localhost:5432/rag")

    # Vector / Embeddings (más adelante)
    embedding_model: str = Field(default="text-embedding-3-small")  # ejemplo OpenAI
    llm_provider: str = Field(default="openai")  # openai|anthropic|local

    # Keys (más adelante)
    openai_api_key: str | None = Field(default=None)
    anthropic_api_key: str | None = Field(default=None)


_settings: Settings | None = None


def get_settings() -> Settings:
    """
    Singleton simple para Settings.
    """
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings