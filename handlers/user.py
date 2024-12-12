from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from db.toy import User, users_db
from filters.callback_f import IsDelBookmarkCallbackData, IsDigitCallbackData
from filters.user_f import IsUserInitialized
from keyboards.bookmarks_kb import create_bookmarks_keyboard, create_edit_keyboard
from keyboards.pagination_kb import create_pagination_kb
from lexicon.ru import Lexicon
from services.file_handling import book

router = Router()
router.message.filter(IsUserInitialized())
router.callback_query.filter(IsUserInitialized())


@router.message(Command(commands="beginning"))
async def beginning_cmd(message: Message, user: User):
    user.page = 1
    await message.answer(
        text=book[user.page], reply_markup=create_pagination_kb(user.page, len(book))
    )


@router.message(Command(commands="continue"))
async def continue_cmd(message: Message, user: User):
    await message.answer()


@router.callback_query(F.data == "forward")
async def next_page(callback: CallbackQuery, user: User):
    user.page += 1
    await callback.message.edit_text(
        text=book[user.page], reply_markup=create_pagination_kb(user.page, len(book))
    )


@router.callback_query()
async def other_callback(callback: CallbackQuery):
    await callback.answer("Пока не работаем 😁")
