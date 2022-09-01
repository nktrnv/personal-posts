from fastapi import APIRouter, Depends, HTTPException, status

from .models import UserRead, UserCreate
from app.database.core import Session, get_session
from . import service

user_router = APIRouter()


@user_router.get('/{username}', response_model=UserRead)
def get_user(username: str, session: Session = Depends(get_session)):
    """Get a user profile by username."""
    user = service.get_by_username(session=session, username=username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


@user_router.post('/', response_model=UserRead)
def sign_up(user_in: UserCreate, session: Session = Depends(get_session)):
    """Register user."""
    return service.create(session=session, user_in=user_in)

