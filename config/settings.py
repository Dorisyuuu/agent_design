import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "your_key_here")
    model_name: str = "gpt-4o-mini"

settings = Settings()
