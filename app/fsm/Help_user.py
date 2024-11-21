from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from keyboards.main_kb import del_kb
from create_bot import bot, admin_id
from aiogram import types
from fsm.states import Help_users



async def register_user_state1(msg: types.Message, state: FSMContext): 
    try:
        if msg.text != "Отмена":
            await bot.send_message(msg.from_user.id, "Твоё сообщение отправлено, постараемся помочь в ближайшеее время")
            await bot.send_message(admin_id, f"@{msg.from_user.username} проблема:\n\n{msg.text}")
        else:
            await bot.send_message(msg.from_user.id, "Обращайся", reply_markup= del_kb)
        await state.finish()
    except BaseException:
        await bot.send_message(msg.from_user.id, 'Произошла ошибка\n\nПопробуйте позднее')
        await state.finish()


def register_gpt_help_fsm(dp: Dispatcher):
    dp.register_message_handler(
        register_user_state1, state=Help_users.help)
