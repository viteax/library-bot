from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message

from db.toy import User, users_db


class IsUserInitialized(BaseFilter):
    async def __call__(self, event: Message | CallbackQuery) -> bool | User:
        if user := users_db.get(event.from_user.id):
            return {"user": user}
        return False
