from app.database.core import Session
from .models import Post, PostCreate


def create(session: Session, post_in: PostCreate, user_id: int) -> Post:
    post = Post(**post_in.dict(), user_id=user_id)
    session.add(post)
    session.commit()
    return post


def get_by_id(session: Session, post_id: int) -> Post:
    return session.query(Post).get(post_id)