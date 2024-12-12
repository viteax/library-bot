import asyncio
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class SlowpokeMiddleware(BaseMiddleware):
    def __init__(self, sleep_sec: int):
        self.sleep_sec = sleep_sec

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        await asyncio.sleep(self.sleep_sec)
        result = await handler(event, data)
        print(f"Я поспал {self.sleep_sec}")
        return result
