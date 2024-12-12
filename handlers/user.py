from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from db.toy import User
from filters.callback_f import IsDelBookmarkCallbackData, IsDigitCallbackData
from filters.user_f import IsUserInitialized
from keyboards.bookmarks_kb import create_bookmarks_keyboard, create_edit_keyboard
from keyboards.pagination_kb import create_pagination_kb
from lexicon.ru import Lexicon
from services.file_handling import book

router = Router()
router.message.filter(IsUserInitialized())
router.callback_query.filter(IsUserInitialized())


async def show_page_message(message: Message, page):
    await message.answer(
        text=book[page], reply_markup=create_pagination_kb(page, len(book))
    )


async def show_page_callback(callback: CallbackQuery, page):
    await callback.message.edit_text(
        text=book[page], reply_markup=create_pagination_kb(page, len(book))
    )


@router.message(Command("beginning"))
async def beginning_cmd(message: Message, user: User):
    user.page = 1
    await show_page_message(message, user.page)


@router.message(Command("continue"))
async def continue_cmd(message: Message, user: User):
    await show_page_message(message, user.page)


@router.message(Command("bookmarks"))
async def bookmarks_cmd(message: Message, user: User):
    await message.answer(
        "Ваши закладки:", reply_markup=create_bookmarks_keyboard(*user.bookmarks)
    )


@router.callback_query(F.data == "forward")
async def next_page(callback: CallbackQuery, user: User):
    user.page += 1
    await show_page_callback(callback, user.page)


@router.callback_query(F.data == "backward")
async def prev_page(callback: CallbackQuery, user: User):
    user.page -= 1
    await show_page_callback(callback, user.page)


@router.callback_query(lambda cb: "/" in cb.data and cb.data.replace("/", "").isdigit())
async def add_or_del_bookmark(callback: CallbackQuery, user: User):
    page = int(callback.data.split("/")[0])
    if page not in user.bookmarks:
        user.bookmarks.add(page)
        await callback.answer("Страница добавлена в закладки")
    else:
        user.bookmarks.remove(page)
        await callback.answer("Страница удалена из закладок")


@router.callback_query(F.data == "edit_bookmarks")
async def edit_bookmarks(callback: CallbackQuery, user: User):
    await callback.message.edit_text(
        text=Lexicon.EDIT_BOOKMARKS, reply_markup=create_edit_keyboard(*user.bookmarks)
    )


@router.callback_query(IsDigitCallbackData())
async def to_page_no(callback: CallbackQuery, page_no: int):
    await show_page_callback(callback, page_no)


@router.callback_query(IsDelBookmarkCallbackData())
async def del_bookmark(callback: CallbackQuery, user: User, page_no: int):
    user.bookmarks.remove(page_no)
    await callback.message.edit_reply_markup(
        reply_markup=create_edit_keyboard(*user.bookmarks)
    )


@router.callback_query(F.data == "cancel")
async def cancel(callback: CallbackQuery, user: User):
    await callback.message.edit_text(text=Lexicon.CANCEL_TEXT)


@router.callback_query(F.data == "book_limit")
async def book_limit(callback: CallbackQuery):
    await callback.answer("А дальше ничего нет) 😁")


@router.callback_query()
async def other_callback(callback: CallbackQuery):
    await callback.answer("Пока не работаем 😁")
