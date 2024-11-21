from db import session
from db.models import User


def get_user_by_id(chat_id: int) -> User:
    return session.query(User).filter(User.chat_id == chat_id).first()
