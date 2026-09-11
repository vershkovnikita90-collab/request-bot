from datetime import datetime
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from states import RequestForm
from keyboards import main_menu
from database import add_request
from config import ADMIN_ID

def register(dp, bot):
    @dp.callback_query(F.data == "request")
    async def request_start(callback: types.CallbackQuery, state: FSMContext):
        await callback.message.edit_text("Напиши своё имя:")
        await state.set_state(RequestForm.name)
        await callback.answer()

    @dp.message(RequestForm.name)
    async def get_name(message: types.Message, state: FSMContext):
        await state.update_data(name=message.text)
        await message.answer("Отлично. Теперь напиши свой телефон:")
        await state.set_state(RequestForm.phone)

    @dp.message(RequestForm.phone)
    async def get_phone(message: types.Message, state: FSMContext):
        data = await state.get_data()
        name = data.get("name")
        phone = message.text
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

        add_request(
            user_id=message.from_user.id,
            username=message.from_user.username,
            name=name,
            phone=phone,
            created_at=created_at
        )

        await bot.send_message(
            ADMIN_ID,
            f"🔥 Новая заявка!\n\n"
            f"Имя: {name}\n"
            f"Телефон: {phone}\n"
            f"Юзер: @{message.from_user.username or 'без username'}\n"
            f"ID: {message.from_user.id}"
        )

        await message.answer(
            "Спасибо! Заявка принята. Я свяжусь с тобой в ближайшее время.",
            reply_markup=main_menu()
        )
        await state.clear()