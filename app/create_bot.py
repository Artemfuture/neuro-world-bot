import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram import Bot


logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

admin_id = "id"
bot = Bot(token="token")
dp = Dispatcher(bot, storage=storage)
