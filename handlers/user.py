from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

from db.toy import user_dict_template, users_db
from filters.callback_f import IsDelBookmarkCallbackData, IsDigitCallbackData
from keyboards.bookmarks_kb import create_bookmarks_keyboard, create_edit_keyboard
from keyboards.pagination_kb import create_pagination_kb
from lexicon.ru import Lexicon
from services.file_handling import book

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(Lexicon.START)
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


@router.message(Command(commands="help"))
async def help_cmd(message: Message):
    await message.answer(Lexicon.HELP)


@router.message(Command(commands="beginning"))
async def beginning_cmd(message: Message):
    users_db[message.from_user.id]["page"] = 1
    text = book[1]
    await message.answer(text=text, reply_markup=create_pagination_kb(1, len(book)))


@router.message(Command(commands="continue"))
async def continue_cmd(message: Message):
    await message.answer()
