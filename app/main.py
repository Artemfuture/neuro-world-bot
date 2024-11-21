from handlers.callback_handler import register_callback_handlers
from handlers.message_handler import register_message_handlers
from handlers.function_handler import register_function_handlers
from fsm.Gpt_image import register_gpt_image_fsm
from fsm.Black_to_white import register_gpt_black_to_white_fsm
from fsm.Help_user import register_gpt_help_fsm
from db.models import create_tables
from aiogram.utils import executor
from create_bot import dp


register_gpt_help_fsm(dp)
register_callback_handlers(dp)
register_gpt_image_fsm(dp)
register_function_handlers(dp)
register_message_handlers(dp)
register_gpt_black_to_white_fsm(dp)

if __name__ == "__main__":
    create_tables()
    executor.start_polling(dp, skip_updates=True)

