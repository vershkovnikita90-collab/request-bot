from aiogram import types, F
from aiogram.filters import CommandStart
from keyboards import main_menu

def register(dp):
    @dp.message(CommandStart())
    async def start(message: types.Message):
        await message.answer(
            f"Привет, {message.from_user.first_name}!\n\n"
            "Я бот для приёма заявок. Помогу оставить заявку на услугу или узнать подробнее.",
            reply_markup=main_menu()
        )

    @dp.callback_query(F.data == "back")
    async def back_to_menu(callback: types.CallbackQuery):
        await callback.message.edit_text(
            "Главное меню. Выбери, что тебя интересует:",
            reply_markup=main_menu()
        )
        await callback.answer()