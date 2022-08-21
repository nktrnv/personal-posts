from fastapi import APIRouter, Depends, HTTPException, status

from app.database.core import Session, get_session
from .models import PostCreate, PostRead
from . import service

post_router = APIRouter()


@post_router.post('/', response_model=PostRead)
def create_post(post_in: PostCreate, session: Session = Depends(get_session)):
    """Create new post."""
    current_user_id = 1
    return service.create(
        session=session, user_id=current_user_id, post_in=post_in)


@post_router.get('/{post_id}', response_model=PostRead)
def get_post(post_id: int, session: Session = Depends(get_session)):
    """Get a post by id."""
    post = service.get_by_id(session=session, post_id=post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return post
