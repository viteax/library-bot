import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Импортируем роутеры
# ...
# Импортируем миддлвари
# ...
# Импортируем вспомогательные функции для создания нужных объектов
# ...
# from keyboards.main_menu import set_main_menu
from config import Config, load_config

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="[{asctime}] #{levelname:8} {filename}:{lineno} - {name} - {message}",
        style="{",
    )
    logger.info("Starting bot")

    config: Config = load_config()

    # Инициализируем объект хранилища
    # storage = ...

    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    # Инициализируем другие объекты (пул соединений с БД, кеш и т.п.)
    # ...

    # Помещаем нужные объекты в workflow_data диспетчера
    # dp.workflow_data.update(...)

    # Настраиваем главное меню бота
    # await set_main_menu(bot)

    # Регистриуем роутеры
    logger.info("Подключаем роутеры")
    # ...

    # Регистрируем миддлвари
    logger.info("Подключаем миддлвари")
    # ...

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
