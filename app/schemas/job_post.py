from pydantic import BaseModel
from typing import List, Optional

class JobPostBase(BaseModel):
    title: str
    company: str
    location: str | None = None
    description: str | None = None
    url: str | None = None
    tags: Optional[List[str]] = []

class JobPostCreate(JobPostBase):
    pass

class JobPostOut(JobPostBase):
    id: int

    class Config:
        orm_mode = True
        