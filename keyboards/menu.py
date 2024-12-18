from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.ru import COMMANDS


async def set_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description,
        )
        for command, description in COMMANDS.items()
    ]
    await bot.set_my_commands(main_menu_commands)
