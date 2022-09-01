from fastapi import APIRouter, Depends, HTTPException, status

from app.database.core import Session, get_session
from app.user import service as user_service
from app.user.models import UserRead
from . import service

subscription_route = APIRouter()


@subscription_route.post('/{username}/subscription')
def subscribe(username: str, session: Session = Depends(get_session)):
    """Subscribe to a user by username."""
    current_user_id = 1
    user = user_service.get_by_username(session=session, username=username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    service.subscribe(
        session=session, user=user, subscriber_id=current_user_id)


@subscription_route.delete('/{username}/subscription')
def unsubscribe(username: str, session: Session = Depends(get_session)):
    """Unsubscribe from a user by username."""
    current_user_id = 1
    user = user_service.get_by_username(session=session, username=username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    service.unsubscribe(
        session=session, user=user, subscriber_id=current_user_id)


@subscription_route.get(
    '/{username}/subscribers', response_model=list[UserRead])
def get_subscribers(username: str, session: Session = Depends(get_session)):
    """Get user's subscribers by username."""
    user = user_service.get_by_username(session=session, username=username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return service.get_subscribers(user=user)


@subscription_route.get(
    '/{username}/subscriptions', response_model=list[UserRead])
def get_subscriptions(username: str, session: Session = Depends(get_session)):
    """Get user's subscriptions by username."""
    user = user_service.get_by_username(session=session, username=username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return service.get_subscriptions(user=user)

