from aiogram.dispatcher import Dispatcher
from keyboards.main_kb import choice_neuronet, text_keyboard, img_keyboard
from create_bot import bot
from aiogram import types
from db.update import update_gpt_text, update_gpt_img ,  update_subscribe
from aiogram.utils.exceptions import BotBlocked


async def callback_handler(msg: types.CallbackQuery):
    await msg.answer()
    if msg.data == "choice_gpt":
        await bot.send_message(msg.from_user.id, f"Выбери нейросеть по умолчанию для генерации текста и картинок", reply_markup=choice_neuronet)
    elif msg.data.startswith("gptt"):
        neiroset = msg.data.split("_")[-1]
        update_gpt_text(chat_id=msg.from_user.id, gpt=neiroset) 
        await bot.send_message(msg.from_user.id, f"Ты выбрал {neiroset}\n\nТеперь ты можешь задавать любые вопросы\n\nДля изменения нейросети воспользуйся меню")
    elif msg.data.startswith("gpti"):
        neiroset = msg.data.split("_")[-1]
        update_gpt_img(chat_id=msg.from_user.id, gpt=neiroset) 
        await bot.send_message(msg.from_user.id, f"Ты выбрал {neiroset}\n\nТеперь ты можешь генерировать любые картинки\n\nДля изменения нейросети воспользуйся меню")

    elif msg.data == "text_gpt":
        await bot.send_message(msg.from_user.id, "Выбирай нейросеть для генерации текста", reply_markup= text_keyboard(msg.from_user.id))

    elif msg.data == "image_gpt":
        await bot.send_message(msg.from_user.id, "Выбирай нейросеть для создания изображения", reply_markup= img_keyboard(msg.from_user.id))

    elif msg.data == "buy":
        await bot.send_invoice(chat_id=msg.from_user.id,
                               title='Подписка',
                               description='Покупай доступ на месяц👇👇👇',
                               payload="subscribe",
                               provider_token="401643678:TEST:7961571b-581f-4aad-b83b-021a93a0c349", 
                               currency='RUB',
                               start_parameter='test_bot',
                               prices=[types.LabeledPrice('Руб', 299_00)]
                               )


async def precheckout_callback(update: types.PreCheckoutQuery):
    try:
        await bot.answer_pre_checkout_query(update.id, True)
    except BotBlocked:
        pass


async def success_payment(msg: types.PreCheckoutQuery):
    try:
        await bot.send_message(msg.from_user.id, 'Ты купил доступ на месяц')
        update_subscribe(msg.from_user.id)
    except BotBlocked:
        pass


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(callback_handler)
    dp.register_pre_checkout_query_handler(precheckout_callback)
    dp.register_message_handler(
        success_payment, content_types=types.ContentType.SUCCESSFUL_PAYMENT)
