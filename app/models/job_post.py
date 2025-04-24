from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class JobPost(Base):
    __tablename__ = "job_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    location = Column(String,  nullable=True)
    description = Column(Text, nullable=True)
    url = Column(String, nullable=True, unique=True)
    