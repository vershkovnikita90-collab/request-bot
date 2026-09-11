from aiogram import types, F
from keyboards import services_menu, back_menu

def register(dp):
    @dp.callback_query(F.data == "services")
    async def show_services(callback: types.CallbackQuery):
        await callback.message.edit_text(
            "Что я делаю:\n\n"
            "• Парсинг сайтов — сбор товаров, цен, контактов\n"
            "• Telegram-боты — под заказ, любой сложности\n"
            "• Автоматизация Excel — убираю рутину\n\n"
            "Выбери, что тебе нужно:",
            reply_markup=services_menu()
        )
        await callback.answer()

    @dp.callback_query(F.data.startswith("srv_"))
    async def service_detail(callback: types.CallbackQuery):
        service = callback.data.replace("srv_", "")
        texts = {
            "parsing": "Парсинг сайтов\n\nСобираю товары, цены, контакты с любых сайтов. Обход блокировок, прокси, капчи. Выгрузка в Excel или CSV.\n\nСрок: от 1 дня.",
            "bots": "Telegram-боты\n\nДелаю ботов для приёма заявок, рассылок, уведомлений, оплат. С админ-панелью и базой данных.\n\nСрок: от 2 дней.",
            "excel": "Автоматизация Excel\n\nЧищу данные, строю отчёты, объединяю таблицы, убираю ручную работу.\n\nСрок: от 1 дня.",
        }
        await callback.message.edit_text(
            texts.get(service, "Услуга не найдена."),
            reply_markup=back_menu()
        )
        await callback.answer()

    @dp.callback_query(F.data == "about")
    async def about(callback: types.CallbackQuery):
        await callback.message.edit_text(
            "О нас\n\n"
            "Python-разработчик. Делаю парсинг, ботов и автоматизацию под ключ.\n"
            "Работаю быстро, даю гарантию.\n\n"
            "Связь: @твой_телеграм",
            reply_markup=back_menu()
        )
        await callback.answer()