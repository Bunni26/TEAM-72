"""Application configuration using Pydantic Settings."""
from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application
    APP_NAME: str = "AI Customer Support"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # API Keys
    OPENAI_API_KEY: str = ""
    PINECONE_API_KEY: str = ""
    PINECONE_ENVIRONMENT: str = "us-east-1"
    PINECONE_INDEX_NAME: str = "customer-support"
    
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@postgres:5432/support_db"
    DATABASE_URL_SYNC: str = "postgresql://postgres:postgres@postgres:5432/support_db"
    
    # Vector DB Settings
    VECTOR_DB_TYPE: str = "chroma"  # "pinecone" or "chroma"
    CHROMA_PERSIST_DIR: str = "/app/data/chroma"
    
    # OpenAI Settings
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"
    OPENAI_CHAT_MODEL: str = "gpt-4o-mini"
    EMBEDDING_DIMENSION: int = 1536
    
    # RAG Settings
    RAG_TOP_K: int = 5
    RAG_SIMILARITY_THRESHOLD: float = 0.7
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50
    
    # n8n Integration
    N8N_WEBHOOK_URL: str = "http://n8n:5678/webhook"
    N8N_API_KEY: Optional[str] = None
    
    # External Services
    SENTRY_DSN: Optional[str] = None
    SMTP_HOST: str = "smtp.sendgrid.net"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    
    # Redis (optional)
    REDIS_URL: str = "redis://redis:6379/0"
    
    # Storage
    STORAGE_TYPE: str = "local"  # "local" or "minio"
    MINIO_ENDPOINT: str = "minio:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"
    LOCAL_STORAGE_PATH: str = "/app/data/uploads"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


settings = get_settings()
