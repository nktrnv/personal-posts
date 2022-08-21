from app.database.core import Session
from app.user.models import User
from app.user import service as user_service


def subscribe(session: Session, user: User, subscriber_id: int) -> None:
    subscriber = user_service.get_by_id(session=session, user_id=subscriber_id)
    user.subscribers.append(subscriber)
    session.commit()


def unsubscribe(session: Session, user: User, subscriber_id: int) -> None:
    subscriber = user_service.get_by_id(session=session, user_id=subscriber_id)
    user.subscribers.remove(subscriber)
    session.commit()


def get_subscribers(user: User) -> list[User]:
    return user.subscribers


def get_subscriptions(user: User) -> list[User]:
    return user.subscriptions


def get_subscribers_count(user: User) -> int:
    return len(user.subscribers)


def get_subscriptions_count(user: User) -> int:
    return len(user.subscriptions)
