from aiogram import types
from aiogram.filters import Command
from config import ADMIN_ID
from database import get_last_requests

def register(dp):
    @dp.message(Command("list"))
    async def list_requests(message: types.Message):
        if message.from_user.id != ADMIN_ID:
            return
        rows = get_last_requests()
        if not rows:
            await message.answer("Заявок пока нет.")
            return

        text = "Последние заявки:\n\n"
        for r in rows:
            text += f"#{r[0]} | {r[1]} | {r[2]} | {r[3]}\n"
        await message.answer(text)