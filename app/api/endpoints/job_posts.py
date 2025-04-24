from fastapi import APIRouter, Depends, HTTPException, Header, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.schemas.job_post import JobPostCreate, JobPostOut
from app.crud import job_post as crud
from app.db.deps import get_db
from app.services.job_importer import scrape_and_store_jobs
from app.scraper.remoteok import fetch_remoteok_jobs
from app.scraper.weworkremotely import fetch_weworkremotely_jobs
from typing import List

router = APIRouter()

@router.get("/", response_model=List[JobPostOut])
async def read_all(
    title: str | None = Query(None),
    company: str | None = Query(None),
    location: str | None = Query(None),
    tags: list[str] | None = Query(None),
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_all_job_posts(db, title=title, company=company, location=location, tags=tags)

@router.get("/{job_id}", response_model=JobPostOut)
async def read_one(job_id: int, db: AsyncSession = Depends(get_db)):
    job = await crud.get_job_post(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/", response_model=JobPostOut)
async def create(job: JobPostCreate, db: AsyncSession = Depends(get_db), x_token: str = Header(...)):
    if x_token != settings.scrape_secret_token:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    return await crud.create_job_post(db, job)

@router.put("/{job_id}", response_model=JobPostOut)
async def update(job_id: int, job: JobPostCreate, db: AsyncSession = Depends(get_db), x_token: str = Header(...)):
    if x_token != settings.scrape_secret_token:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    updated = await crud.update_job_post(db, job_id, job)

    if not updated:
        raise HTTPException(status_code=404, detail="Job not found")
    return updated

@router.delete("/{job_id}")
async def delete(job_id: int, db: AsyncSession = Depends(get_db), x_token: str = Header(...)):
    if x_token != settings.scrape_secret_token:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    deleted = await crud.delete_job_post(db, job_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"ok": True}

@router.post("/scrape-remoteok")
async def scrape_jobs(db: AsyncSession = Depends(get_db), x_token: str = Header(...)):
    if x_token != settings.scrape_secret_token:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    result = await scrape_and_store_jobs(fetch_remoteok_jobs, db)
    return result

# Commented out
#@router.post("/scrape-wwr")
#async def scrape_jobs(db: AsyncSession = Depends(get_db),x_token: str = Header(...)):
#    if x_token != settings.scrape_secret_token:
#        raise HTTPException(status_code=403, detail="Forbidden")
#
#    result = await scrape_and_store_jobs(fetch_weworkremotely_jobs, db)
#    return result
