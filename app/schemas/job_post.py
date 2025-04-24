from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional

class JobPostBase(BaseModel):
    title: str
    company: str
    location: str | None = None
    description: str | None = None
    url: str | None = None
    tags: Optional[List[str]] = Field(default_factory=list)

class JobPostCreate(JobPostBase):
    pass

class JobPostOut(JobPostBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
        