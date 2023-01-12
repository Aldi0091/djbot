from aiogram import types

from .data_fetcher import save_token
from .app import dis
from . import messages
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class Form(StatesGroup):
    name = State()


@dis.message_handler(commands=["start", "help"])
async def send(message: types.Message):
    await Form.name.set()
    
    await message.reply("SEND YOUR NAME")

@dis.message_handler(state=Form.name)
async def process_message(message: types.Message, state: FSMContext):

    await state.finish()
    res = message.text 
    server = await save_token(res)
    print(server)
    await message.reply(server)
    