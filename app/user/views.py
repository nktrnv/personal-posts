from fastapi import APIRouter, Depends

from .models import UserRead
from app.database.core import Session, get_session
from . import service

user_router = APIRouter()


@user_router.get('/{username}', response_model=UserRead)
def get_user(username: str, session: Session = Depends(get_session)):
    """Get user profile by username."""
    return service.get_by_username(session=session, username=username)
