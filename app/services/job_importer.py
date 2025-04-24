from app.schemas.job_post import JobPostCreate
from app.crud.job_post import create_job_post, get_all_job_posts
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Callable

async def scrape_and_store_jobs(scraper_func: Callable[[], list[dict]],db: AsyncSession):
    jobs = scraper_func()
    existing_jobs = await get_all_job_posts(db)
    existsing_urls = {job.url for job in existing_jobs}

    added = 0
    for job in jobs:
        if job["url"] not in existsing_urls:
            job_data = JobPostCreate(**job)
            await create_job_post(db, job_data)
            added += 1

    return{"Added": added, "Total scraped": len(jobs)}
