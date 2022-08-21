from fastapi import APIRouter

from app.user.views import user_router
from app.subscription.views import subscription_route

api_router = APIRouter()
api_router.include_router(user_router, prefix='/users', tags=['users'])
api_router.include_router(
    subscription_route, prefix='/users', tags=['subscriptions'])
