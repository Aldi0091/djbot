from aiogram import executor
from bot_app import dis




if __name__ == "__main__":
    executor.start_polling(dis, skip_updates=True)