from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from db.get import get_user_by_id

main_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(
        text='Выбрать нейросеть',
        callback_data='choice_gpt'
    )
)

choice_neuronet = InlineKeyboardMarkup(row_width=1).add(
            InlineKeyboardButton(
                text="Нейросети для текста",
                callback_data="text_gpt"
            ),
            InlineKeyboardButton(
                text="Нейросеть для изображений",
                callback_data="image_gpt"
    ))


def text_keyboard(chat_id: int) -> InlineKeyboardMarkup:
    user = get_user_by_id(chat_id)
    if user.gpt_text is not None:
        neiroset = user.gpt_text
        choice_neuronet = InlineKeyboardMarkup(row_width=1).add(
            InlineKeyboardButton(
                text='Yandex_gpt ✅' if neiroset in "Yandex_gpt" else "Yandex_gpt ❌",
                callback_data='gptt_Yandex'
            ),
            InlineKeyboardButton(
                text="Gigachat ✅" if neiroset in "Gigachat" else "Gigachat ❌",
                callback_data="gptt_Gigachat"
            ))
    
    else:
        choice_neuronet = InlineKeyboardMarkup(row_width=1).add(
            InlineKeyboardButton(
                text='Yandex_gpt',
                callback_data='gptt_Yandex'
            ),
            InlineKeyboardButton(
                text="Gigachat",
                callback_data="gptt_Gigachat"
            ))
    return choice_neuronet


def img_keyboard(chat_id: int) -> InlineKeyboardMarkup:
    user = get_user_by_id(chat_id)
    if user.img_gpt is not None:
        neiroset = user.img_gpt
        choice_neuronet = InlineKeyboardMarkup(row_width=1).add(
            InlineKeyboardButton(
                text='Yandex_art ✅' if neiroset in "Yandex_art" else "Yandex_gpt ❌",
                callback_data='gpti_Yandex'
            ),
            InlineKeyboardButton(
                text="Kandinsky ✅" if neiroset in "Kandinsky" else "Kandinsky ❌",
                callback_data="gpti_Kandinsky"
            ))
    else:
        choice_neuronet = InlineKeyboardMarkup(row_width=1).add(
            InlineKeyboardButton(
                text='Yandex_art' ,
                callback_data='gpti_Yandex'
            ),
            InlineKeyboardButton(
                text="Kandinsky",
                callback_data="gpti_Kandinsky"
            ))
    return choice_neuronet





cancel_kb = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(
        text='Отмена'
    )
)
buy_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(
        text='Купить',
        callback_data='buy'
    )
)

del_kb = ReplyKeyboardRemove()

def another_neiro_txt(chat_id : int ):
    neiro_txt = get_user_by_id(chat_id).gpt_text
    another_neiro_txt = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(
        text="Отправить запрос в другую нейросеть",
        callback_data="anothertxt_Yandex" if neiro_txt in "Yandex" else "anothertxt_Gigachat",
    ))
    return another_neiro_txt


def another_neiro_img(chat_id : int ):
    neiro_txt = get_user_by_id(chat_id).img_gpt
    another_neiro_txt = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(
        text="Отправить запрос в другую нейросеть",
        callback_data="anotherimg_Yandex" if neiro_txt in "Yandex" else "anotherimg_Kandinsky",
    ))
    return another_neiro_txt