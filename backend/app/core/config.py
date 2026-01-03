"""
Application configuration settings
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings"""

    # Application
    APP_NAME: str = "GermanQuest API"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./germanquest.db"

    # API
    API_V1_PREFIX: str = "/api/v1"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
