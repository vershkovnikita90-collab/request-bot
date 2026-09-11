from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🛠 Услуги", callback_data="services")
    builder.button(text="📞 Оставить заявку", callback_data="request")
    builder.button(text="ℹ️ О нас", callback_data="about")
    builder.adjust(1)
    return builder.as_markup()

def services_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Парсинг сайтов", callback_data="srv_parsing")
    builder.button(text="Telegram-боты", callback_data="srv_bots")
    builder.button(text="Автоматизация Excel", callback_data="srv_excel")
    builder.button(text="⬅️ Назад", callback_data="back")
    builder.adjust(1)
    return builder.as_markup()

def back_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ В меню", callback_data="back")
    return builder.as_markup()