from aiogram.dispatcher import Dispatcher
from keyboards.main_kb import main_kb, choice_neuronet, cancel_kb
from create_bot import bot
from aiogram import types
from db.get import get_user_by_id
from db.create import create_user
from menu_bot import set_defailt_command
from fsm.states import Gpt_image, Black_to_white, Help_users

async def func_start(msg: types.Message):
    await set_defailt_command(bot)
    if get_user_by_id(msg.from_user.id) is not None:
        await bot.send_message(msg.from_user.id, "Задавай свой вопрос нейросети", reply_markup=main_kb)
    else:
        create_user(chat_id=msg.from_user.id, username=msg.from_user.username)
        await bot.send_message(msg.from_user.id, f"Привет {msg.from_user.first_name}!\n\nЭтот Telegram-бот станет твоим помощником в общении с несколькими нейросетями и создании изображений:\n\n🔵 Получи ответы на любые вопросы\n🔵 Сгенерируй уникальные изображения по описанию\n🔵 Преврати черно-белые фотографии в цветные\n🟢 Создай тексты на разных языках\n💡 Найди идеи для творчества и работы\n📚 Обсуди сложные темы и получи советы от нейросети\n🧠 Решай математические задачи любой сложности\n🌐 Переведи тексты на разные языки и обратно\n\nНачинай общение прямо сейчас!", reply_markup=main_kb)


async def func_question(msg: types.Message):
    if get_user_by_id(msg.from_user.id).gpt_text is not None:
        await bot.send_message(msg.from_user.id, "Пришли вопрос")
    else:
        await bot.send_message(msg.from_user.id, "Сначала выбери нейросеть по умолчанию", reply_markup=choice_neuronet)


async def func_gpt(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Выбирай нейросеть", reply_markup=choice_neuronet)


async def func_help(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Напиши свою проблему, мы постараемя решить её как можно быстрее", reply_markup=cancel_kb)
    await Help_users.help.set()

async def funck_image(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Пришли описание картинки:")
    await Gpt_image.text_image.set()

async def funck_bl_wh(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Пришли картинку")
    await Black_to_white.blacktowhite.set()





def register_function_handlers(dp: Dispatcher):
    dp.register_message_handler(func_start, commands="start")
    dp.register_message_handler(func_question, commands="question")
    dp.register_message_handler(func_gpt, commands="gpt") 
    dp.register_message_handler(func_help, commands="help") 
    dp.register_message_handler(funck_image, commands="image")
    dp.register_message_handler(funck_bl_wh, commands="getcolor") # доработать 