from aiogram import types

from .data_fetcher import save_token
from .app import dis, bot
from . import messages
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from postgres.main import Postgres


class Form(StatesGroup):
    name = State()


@dis.message_handler(commands=["start", "help"])
async def send(message: types.Message):
    await Form.name.set()
    await message.reply("SEND YOUR TOKEN")
    

@dis.message_handler(state=Form.name)
async def process_message(message: types.Message, state: FSMContext):

    await state.finish()
    tok = message.text 
    Postgres.insert_id(int(message.from_user.id), str(tok))

 

