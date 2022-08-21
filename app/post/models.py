from datetime import datetime

from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database.core import Base
from app.user.models import UserRead


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='posts')


class PostBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=30)
    text: str

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    created_at: datetime
    user: UserRead


class PostUpdate(PostCreate):
    pass
