from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot


async def set_defailt_command(bot: Bot):
    commands = [
        BotCommand(
            command="/question",
            description="Задать вопрос нейросети"),
        BotCommand(
            command="/gpt",
            description="Сменить нейросеть"),
        BotCommand(
            command="/image",
            description="Сгенерировать картинку"
        ),
        BotCommand(
            command="/getcolor",
            description="Превратить чёрно-белую картинку в цветную"
        ),
        BotCommand(
            command="/help",
            description="Написать в поддержку")]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
