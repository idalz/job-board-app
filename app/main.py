from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from app.core.config import settings
from app.api.endpoints import job_posts
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.deps.admin import verify_admin_token


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

@app.get("/admin-login", response_class=HTMLResponse)
async def admin_login_page(request: Request):
    return templates.TemplateResponse("admin_login.html", {"request": request})

@app.get("/admin-actions", response_class=HTMLResponse)
async def admin_actions(request: Request, token: str = Depends(verify_admin_token)):
    return templates.TemplateResponse("admin_actions.html", {"request": request})

@app.get("/admin-dashboard", response_class=HTMLResponse)
async def admin_dashboard(request: Request, token: str = Depends(verify_admin_token)):
    return templates.TemplateResponse("admin_dashboard.html", {"request": request})
