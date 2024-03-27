import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import apsched
from datetime import datetime, timedelta



async def start():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def cmd_start(message: Message):
        await message.answer('Привет!')
    scheduler = AsyncIOScheduler(timezone="Asia/Novosibirsk")
    scheduler.add_job(apsched.send_message, trigger='cron', hour = 21, minute = 0, start_date = datetime.now(),
                      kwargs={'bot': bot})
    scheduler.start()
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())