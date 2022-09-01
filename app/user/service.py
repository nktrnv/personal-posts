from passlib.hash import bcrypt

from app.database.core import Session
from .models import User, UserCreate


def get_by_username(session: Session, username: str) -> User:
    return session.query(User).filter_by(username=username).one_or_none()


def get_by_id(session: Session, user_id: int) -> User:
    return session.query(User).get(user_id)


def create(session: Session, user_in: UserCreate) -> User:
    user = User(
        **user_in.dict(exclude={'password'}),
        password_hash=_hash_password(user_in.password)
    )
    session.add(user)
    session.commit()
    return user


def _hash_password(password: str) -> str:
    return bcrypt.hash(password)
