from db.init_db import Base, engine, session
from .user import User


def create_tables():
    session.commit()
    # User.__table__.drop(engine)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
