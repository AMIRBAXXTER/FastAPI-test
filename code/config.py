from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Chat Application"
    admin_email: str = "admin@example.com"
    mongo_uri: str = "mongodb://localhost:27017/chat_db"
    secret_key: str = "your_secret_key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()