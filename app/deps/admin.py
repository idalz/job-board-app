from fastapi.responses import RedirectResponse
from fastapi import Header
from app.core.config import settings

# Dependency to verify token before accessing admin routes
async def verify_admin_token(x_token: str = Header(None)):
    if not x_token or x_token != settings.admin_token:
        return RedirectResponse(url='/admin-login') 
    