from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.ru import Lexicon
from services.file_handling import book


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        *[
            InlineKeyboardButton(
                text=f"{button} - {book[button][:100]}",
                callback_data=str(button),
            )
            for button in sorted(args)
        ]
    )
    kb_builder.row(
        InlineKeyboardButton(text="Редактировать", callback_data="edit_bookmarks"),
        InlineKeyboardButton(text="Отменить", callback_data="cancel"),
        width=2,
    )
    return kb_builder.as_markup()


def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        *[
            InlineKeyboardButton(
                text=f"{Lexicon.DEL} {button} - {book[button][:100]}",
                callback_data=f"{button}del",
            )
            for button in sorted(args)
        ]
    )
    kb_builder.row(InlineKeyboardButton(text=Lexicon.CANCEL, callback_data="cancel"))
    return kb_builder.as_markup()
