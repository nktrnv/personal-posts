from fastapi import APIRouter, Depends, HTTPException, status

like_router = APIRouter()
user_like_router = APIRouter()


@like_router.post('/{post_id}/like')
def like_post(post_id: int):
    pass


@like_router.delete('/{post_id}/like')
def remove_post_like(post_id: int):
    pass


@user_like_router.get('/{username}/likes')
def get_user_likes(username: str):
    pass
