from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.job_post import JobPostCreate, JobPostOut
from app.crud import job_post as crud
from app.db.deps import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=JobPostOut)
async def create(job: JobPostCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_job_post(db, job)

@router.get("/", response_model=List[JobPostOut])
async def read_all(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_job_posts(db)

@router.get("/{job_id}", response_model=JobPostOut)
async def read_one(job_id: int, db: AsyncSession = Depends(get_db)):
    job = await crud.get_job_post(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.put("/{job_id}", response_model=JobPostOut)
async def update(job_id: int, job: JobPostCreate, db: AsyncSession = Depends(get_db)):
    updated = await crud.update_job_post(db, job_id, job)
    if not updated:
        raise HTTPException(status_code=404, detail="Job not found")
    return updated

@router.delete("/{job_id}")
async def delete(job_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await crud.delete_job_post(db, job_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"ok": True}
