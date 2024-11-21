from db import session
from db.models import User


def create_user(chat_id: int, username: str):
    try:
        new_user = User(
            chat_id=chat_id,
            username=username
        )
        session.add(
            new_user
        )
        session.commit()
    except Exception as Err:
        print(Err)
        session.rollback()
