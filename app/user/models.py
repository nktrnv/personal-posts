import sqlalchemy as sa
from pydantic import BaseModel, Field

from app.database.core import Base


class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String, unique=True, nullable=False)
    password_hash = sa.Column(sa.String, nullable=False)
    name = sa.Column(sa.String)
    bio = sa.Column(sa.String)


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
