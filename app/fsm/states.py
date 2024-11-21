from aiogram.dispatcher.filters.state import State, StatesGroup


class Gpt_image(StatesGroup):
    text_image = State()


class Black_to_white(StatesGroup):
    blacktowhite = State()

class Help_users(StatesGroup):
    help = State()