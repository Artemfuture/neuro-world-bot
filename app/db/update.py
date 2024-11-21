from db import session
from db.models import User
from db.get import get_user_by_id
from datetime import date, timedelta

 
def update_gpt_text(chat_id: int, gpt: str):
    user = get_user_by_id(chat_id)
    user.gpt_text = gpt
    session.commit()

def update_gpt_img(chat_id: int, gpt: str):
    user = get_user_by_id(chat_id)
    user.img_gpt = gpt
    session.commit()

def update_last_using_text(chat_id : int):
    user = get_user_by_id(chat_id)
    if user.last_using_time == date.today():
        user.limit_text -= 1
    else:
        user.limit_text = 9
        user.limit_yandex_gpt = 1
        user.limit_img = 10
        user.last_using_time = date.today()
    session.commit()

def update_last_using_img(chat_id : int):
    user = get_user_by_id(chat_id)

    if user.last_using_time == date.today():
        user.limit_img -= 1
    else:
        user.limit_text = 10
        user.limit_yandex_gpt = 1
        user.limit_img = 9
        user.last_using_time = date.today()
    session.commit()

def update_last_using_art(chat_id : int):
    user = get_user_by_id(chat_id)
    if user.last_using_time == date.today():
        user.limit_yandex_gpt -= 1
    else:
        user.limit_text = 10
        user.limit_yandex_gpt = 0
        user.limit_img = 10
        user.last_using_time = date.today()
    session.commit()

def update_last_text(chat_id : int, msg : str):
    user = get_user_by_id(chat_id)
    user.last_text = msg

def update_last_img(chat_id : int, msg : str):
    user = get_user_by_id(chat_id)
    user.last_img = msg

def update_subscribe(chat_id: int):  
    user = get_user_by_id(chat_id)
    user.subscribe = date.today() + timedelta(days=30)
    session.commit()