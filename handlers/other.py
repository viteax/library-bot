from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from db.toy import User, users_db
from filters.user_f import IsUserInitialized
from lexicon.ru import Lexicon

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(Lexicon.START)
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = User()


@router.message(Command(commands="help"))
async def help_cmd(message: Message):
    await message.answer(Lexicon.HELP)


@router.message(~IsUserInitialized())
async def send_not_initialized(message: Message):
    await message.answer("Вы не авторизованы, авторизуйтесь командой /start")


@router.message()
async def send_echo(message: Message):
    try:
        await message.copy_to(message.chat.id)
    except TypeError:
        await message.answer(Lexicon.OTHER)
