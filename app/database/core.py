from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

engine = create_engine(settings.database_url)
Session = sessionmaker(bind=engine)
Base = declarative_base()


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
