from pydantic import BaseSettings

class Settings(BaseSettings):
    telegram_bot_token: str
    gemini_api_key: str
    
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
