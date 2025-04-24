from fastapi import Header, HTTPException, status
from app.core.config import settings

async def verify_admin_token(x_token: str = Header(...)):
    if x_token != settings.admin_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid admin token"
        )
    