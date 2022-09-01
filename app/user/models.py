from string import ascii_lowercase, digits

from pydantic import BaseModel, Field, validator
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.core import Base
from app.subscription.models import subscriptions
from app.like.models import likes


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
    posts = relationship('Post', back_populates='user')
    liked_posts = relationship(
        'Post', secondary=likes, back_populates='liked_users')


class UserBase(BaseModel):
    username: str = Field(..., min_length=4, max_length=20)
    name: str | None = Field(None, min_length=1, max_length=30)
    bio: str | None = Field(None, min_length=1, max_length=60)

    @validator('username')
    def check_username(cls, username: str):
        allowed_symbols = list(ascii_lowercase + digits + '_')
        for symbol in username:
            if symbol not in allowed_symbols:
                raise ValueError(
                    'Username must contain only a-z, 0-9 and underscores')
        return username

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    pass
    # subscribers_count: int
    # subscriptions_count: int
