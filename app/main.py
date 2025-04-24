from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from app.core.config import settings
from app.api.endpoints import job_posts
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(
    job_posts.router, 
    prefix=f"{settings.api_v1_str}/job-posts", 
    tags=["Job Posts"]
) 

@app.get("/", response_class=HTMLResponse)
async def get_index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/admin", response_class=HTMLResponse)
async def serve_admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.get("/admin-dashboard", response_class=HTMLResponse)
async def serve_admin_dashboard(request: Request):
    return templates.TemplateResponse("admin_dashboard.html", {"request": request})
