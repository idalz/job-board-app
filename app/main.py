from fastapi import FastAPI, Depends
from app.core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.deps import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": f"{settings.project_name} backend is live!"}

@app.get("/ping-db")
async def ping_db(db: AsyncSession = Depends(get_db)):
    return {"db_status": "connected"}
