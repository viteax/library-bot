from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.ru import Lexicon


def create_pagination_kb(cur_page_no: int, book_len: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(
            text=Lexicon.BACKWARD if not (cur_page_no == 1) else " ",
            callback_data="backward" if not (cur_page_no == 1) else "book_limit",
        ),
        InlineKeyboardButton(
            text=f"{cur_page_no}/{book_len}",
            callback_data=f"{cur_page_no}/{book_len}",
        ),
        InlineKeyboardButton(
            text=Lexicon.FORWARD if not (cur_page_no == book_len) else " ",
            callback_data="forward" if not (cur_page_no == book_len) else "book_limit",
        ),
    ]
    kb_builder.row(*buttons)
    return kb_builder.as_markup()
