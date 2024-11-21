from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from create_bot import bot
from aiogram import types
from fsm.states import Gpt_image
from  db.get import get_user_by_id
from keyboards.main_kb import buy_kb, main_kb, another_neiro_img
from db.update import update_last_using_art, update_last_using_img, update_last_img
from func.kandinsky import kandinsky_gpt
from func.yandex_art import image_gpt
from datetime import date


async def register_user_state1(msg: types.Message, state: FSMContext): 
    try:
        user = get_user_by_id(msg.from_user.id)
        if user is not None and user.img_gpt is not None:
            if (user.limit_text > 0 or user.subscribe > date.today()) and user.img_gpt == "Yandex":
                update_last_using_art(msg.from_user.id)
                update_last_img(chat_id= msg.from_user.id, msg= msg.text)
                answer = image_gpt(msg.text)
                await bot.send_photo(msg.from_user.id, answer, reply_markup= another_neiro_img(msg.from_user.id))
            elif (user.limit_text > 0 or user.subscribe > date.today()) and user.img_gpt == "Kandinsky":
                update_last_using_img(msg.from_user.id)
                update_last_img(chat_id= msg.from_user.id, msg= msg.text)
                answer = kandinsky_gpt(msg.text)
                await bot.send_photo(msg.from_user.id, answer, reply_markup= another_neiro_img(msg.from_user.id))
            else:
                await bot.send_message(msg.from_user.id, "Ты исчерпал ежедневный лимит, попробуй завтра\n\nИли купи доступ на месяц", reply_markup=buy_kb)
        else:
            await bot.send_message(msg.from_user.id, "Вы не выбрали модель для генерации изображения", reply_markup=main_kb)
        await state.finish()

    except BaseException:
        await bot.send_message(msg.from_user.id, 'Произошла ошибка\n\nПопробуйте позднее')
        await state.finish()


def register_gpt_image_fsm(dp: Dispatcher):
    dp.register_message_handler(
        register_user_state1, state=Gpt_image.text_image)
