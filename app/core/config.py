from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    project_name: str
    api_v1_str: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()