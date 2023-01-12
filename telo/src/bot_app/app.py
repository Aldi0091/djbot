from .local_settings import API_KEY
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()



bot = Bot(token=API_KEY)
dis = Dispatcher(bot, storage=storage)

