from aiogram.dispatcher import Dispatcher
from keyboards.main_kb import main_kb, buy_kb, another_neiro_txt
from create_bot import bot
from aiogram import types
from db.get import get_user_by_id
from func.gigchat import gigachat
from func.yandex_gpt import send_gpt_question
from db.update import update_last_using_text, update_last_text
from datetime import date


async def message_handler(msg: types.Message):
    user = get_user_by_id(msg.from_user.id)
    if user is not None and user.gpt_text is not None:
        if user.limit_text > 0 or user.subscribe > date.today():
            update_last_using_text(msg.from_user.id)
            update_last_text(chat_id= msg.from_user.id, msg= msg.text)
            if user.gpt_text == "Yandex":
                await bot.send_message(msg.from_user.id, send_gpt_question(msg.text))
            elif user.gpt_text == "Gigachat":
                await bot.send_message(msg.from_user.id, gigachat(msg.text), reply_markup = another_neiro_txt(msg.from_user.id))
            else:
                await bot.send_message(msg.from_user.id, "Вы не выбрали модель", reply_markup=main_kb)
        else:
            await bot.send_message(msg.from_user.id, "Ты исчерпал ежедневный лимит, попробуй завтра\n\nИли купи доступ на месяц", reply_markup=buy_kb)
    else:
        await bot.send_message(msg.from_user.id, "Я вас не понимаю")


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(message_handler)
