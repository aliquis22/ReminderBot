from aiogram import Bot
from datetime import datetime

async def send_message(bot: Bot):
    await bot.send_message('-1002035455082', 'Всем доброго вечера! Не забудьте отметиться в Confluence')

