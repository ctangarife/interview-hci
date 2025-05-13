#app/core/config/settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Interview Transcription Service"
    DEBUG: bool = True

settings = Settings()