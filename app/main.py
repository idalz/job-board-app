from fastapi import FastAPI, Depends
from app.core.config import settings
from app.api.endpoints import job_posts

app = FastAPI()

app.include_router(
    job_posts.router, 
    prefix=f"{settings.api_v1_str}/job-posts", 
    tags=["Job Posts"]
)
