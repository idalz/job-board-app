from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from app.models.job_post import JobPost
from app.schemas.job_post import JobPostCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def create_job_post(db: AsyncSession, job_post: JobPostCreate) -> JobPost:
    db_post = JobPost(**job_post.model_dump())
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return db_post

async def get_all_job_posts(  
    db: AsyncSession,
    title: str | None = None,
    company: str | None = None,
    location: str | None = None
):
    query = select(JobPost)

    if title:
        query = query.where(JobPost.title.ilike(f"%{title}%"))
    if title:
        query = query.where(JobPost.company.ilike(f"%{company}%"))
    if title:
        query = query.where(JobPost.location.ilike(f"%{location}%"))
    
    result = await db.execute(select(JobPost))
    return result.scalars().all()

async def get_job_post(db: AsyncSession, job_id: int):
    result = await db.execute(select(JobPost).where(JobPost.id == job_id))
    return result.scalar_one_or_none()

async def update_job_post(db: AsyncSession, job_id: int, job_data: JobPostCreate):
    db_post = await get_job_post(db, job_id)
    if db_post:
        for field, value in job_data.model_dump().items():
            setattr(db_post, field, value)
        await db.commit()
        await db.refresh()
    return  db_post

async def delete_job_post(db: AsyncSession, job_id: int):
    db_post = await get_job_post(db, job_id)
    if db_post:
        await db.delete(db_post)
        await db.commit()
    return db_post
