import sqlalchemy as sa

from app.database.core import Base

subscriptions = sa.Table(
    'subscriptions',
    Base.metadata,
    sa.Column(
        'user_id', sa.Integer, sa.ForeignKey('users.id'), primary_key=True),
    sa.Column(
        'subscriber_id', sa.Integer, sa.ForeignKey('users.id'),
        primary_key=True)
)
