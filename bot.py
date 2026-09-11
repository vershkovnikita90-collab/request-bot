import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from database import init_db
from handlers import start, services, request, admin

logging.basicConfig(level=logging.INFO)

async def main():
    init_db()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    start.register(dp)
    services.register(dp)
    request.register(dp, bot)
    admin.register(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())