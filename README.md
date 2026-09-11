# 🤖 Request Bot — Telegram-бот для приёма заявок

**Бот принимает заявки от клиентов, сохраняет их в базу и мгновенно уведомляет администратора.**

[![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)](https://python.org)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-green?style=for-the-badge)](https://aiogram.dev)
[![SQLite](https://img.shields.io/badge/SQLite-database-lightgrey?style=for-the-badge&logo=sqlite)](https://sqlite.org)

---

## 🚀 Возможности

- **Приём заявок** — пошаговый диалог: имя → телефон
- **Уведомления админа** — мгновенное оповещение в Telegram о новой заявке
- **История заявок** — команда `/list` для просмотра последних обращений
- **Инлайн-меню** — удобная навигация по кнопкам (услуги, о нас)
- **База данных** — все заявки сохраняются в SQLite

---

## 🛠 Технологии

- **Python 3.13**
- **aiogram 3.x** — асинхронная библиотека для Telegram-ботов
- **SQLite** — хранение заявок
- **python-dotenv** — безопасное хранение токена
- **aiohttp-socks** — поддержка прокси

---

## 📦 Быстрый старт

1. **Клонируй репозиторий:**
   ```bash
   git clone https://github.com/vershkovnikita90-collab/request-bot.git
   cd request-bot