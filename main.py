import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import Config, load_config
from handlers import other, user
from keyboards.menu import set_menu
from lexicon import en, ru
from middlewares.i18n import TranslatorMiddleware
from middlewares.throttling import ThrottlingMiddleware

logger = logging.getLogger(__name__)

translations = {
    "default": ru.Lexicon,
    "ru": ru.Lexicon,
    "en": en.Lexicon,
}


async def main() -> None:
    logger.info("Starting bot")

    config: Config = load_config()

    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    await set_menu(bot)

    dp.include_router(user.router)
    dp.include_router(other.router)

    dp.update.middleware(ThrottlingMiddleware())
    dp.update.middleware(TranslatorMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, _translations=translations)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="{filename}:{lineno} #{levelname:8} [{asctime}] - {name} - {message}",
        style="{",
    )
    asyncio.run(main())
