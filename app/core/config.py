from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from dotenv import load_dotenv

load_dotenv()
class Settings(BaseSettings):
    project_name: str
    api_v1_str: str
    admin_token: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
