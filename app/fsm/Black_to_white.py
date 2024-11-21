from aiogram.dispatcher import FSMContext
import os.path
from aiogram import Dispatcher
from create_bot import bot
from aiogram import types
from .states import Black_to_white

from func.black_to_white import black_to_color


from aiogram.types import ContentType


async def register_user_state1(msg: types.Message, state: FSMContext):
    try:
        if msg.content_type == ContentType.PHOTO:
            await msg.photo[-1].download(destination_file= f"path")
            # await bot.download_file_by_id(file_id=msg.photo)
            black_to_color(msg.from_user.id)
            if os.path.exists(f"path") and os.path.exists(f"path"):
                media = types.MediaGroup()
                media.attach_photo(types.InputFile(f'path'))
                media.attach_photo(types.InputFile(f'path'))
                await bot.send_media_group(msg.from_user.id, media= media)
            await state.finish()

    except BaseException:
        await bot.send_message(msg.from_user.id, 'Произошла ошибка\n\nПопробуйте позднее')
        await state.finish()


def register_gpt_black_to_white_fsm(dp: Dispatcher):
    dp.register_message_handler(
        register_user_state1, state=Black_to_white.blacktowhite, content_types=[
                                ContentType.PHOTO])
