import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN, PROXY_URL
from database import init_db
from handlers import start, services, request, admin

logging.basicConfig(level=logging.INFO)


async def main():
    init_db()

    session = AiohttpSession(proxy=PROXY_URL) if PROXY_URL else None
    bot = Bot(token=BOT_TOKEN, session=session)
    dp = Dispatcher(storage=MemoryStorage())

    start.register(dp)
    services.register(dp)
    request.register(dp, bot)
    admin.register(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())