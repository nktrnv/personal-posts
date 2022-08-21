from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.core import Base
from app.subscription.models import subscriptions


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    name = Column(String)
    bio = Column(String)
    subscribers = relationship(
        'User',
        secondary=subscriptions,
        primaryjoin=(id == subscriptions.c.user_id),
        secondaryjoin=(id == subscriptions.c.subscriber_id),
        backref='subscriptions'
    )


class UserBase(BaseModel):
    username: str = Field(..., min_length=4, max_length=20)
    name: str | None = Field(None, min_length=1, max_length=30)
    bio: str | None = Field(None, min_length=1, max_length=60)

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    pass
    # subscribers_count: int
    # subscriptions_count: int
