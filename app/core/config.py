from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from dotenv import load_dotenv

load_dotenv()
class Settings(BaseSettings):
    project_name: str
    api_v1_str: str
    database_url: str
    scrape_secret_token: str

    model_config = ConfigDict(env_file=".env")

settings = Settings()
