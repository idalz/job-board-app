from pydantic import BaseModel

class JobPostBase(BaseModel):
    title: str
    company: str
    location: str | None = None
    description: str | None = None
    url: str | None = None

class JobPostCreate(JobPostBase):
    pass

class JobPostOut(JobPostBase):
    id: int

    class Config:
        orm_mode = True
        