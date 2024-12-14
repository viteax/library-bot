from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User


class TranslatorMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        user: User = data.get("event_from_user")
        if not user:
            return await handler(event, data)

        translations: dict[str, object] = data.get("_translations")
        data["i18n"] = translations.get(user.language_code, translations["default"])
        return await handler(event, data)
