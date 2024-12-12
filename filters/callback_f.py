from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.isdigit():
            return {"page_no": int(callback.data)}
        return False


class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        if callback.data.endswith("del") and callback.data[:-3].isdigit():
            return {"page_no": int(callback.data[:-3])}
        return False
