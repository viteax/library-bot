from aiogram import Router
from aiogram.types import Message

from lexicon.ru import Lexicon

router = Router()


@router.message()
async def send_echo(message: Message):
    try:
        await message.copy_to(message.chat.id)
    except TypeError:
        await message.answer(Lexicon.OTHER)
