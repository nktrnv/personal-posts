from app.database.core import Session
from .models import User


def get_by_username(session: Session, username: str) -> User:
    return session.query(User).filter_by(username=username).one_or_none()


def get_by_id(session: Session, user_id: int) -> User:
    return session.query(User).get(user_id)
