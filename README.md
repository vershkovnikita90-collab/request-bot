
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
2. **Установи зависимости:**
   ```bash
   pip install -r requirements.txt
3. **Создай файл `.env` в корне проекта и вставь свои данные:**
BOT_TOKEN=твой_токен_от_botfather
ADMIN_ID=твой_id_от_userinfobot
PROXY_URL=socks5://ip:port
4. **Запусти бота:**
```bash
python bot.py

**Что изменилось:**
- Убрал слова `text` и `bash` **перед** блоками — они там лишние, потому что ты уже пишешь ` ``` ` для подсветки
- Добавил отступы, чтобы блоки кода визуально были внутри пункта списка

---

Если хочешь ещё красивее — добавь в конце README блок с примером работы. Типа:

```markdown
---

## 📸 Пример работы

1. Пользователь нажимает `/start`
2. Выбирает «Оставить заявку»
3. Вводит имя и телефон
4. Админ получает уведомление
5. Админ вводит `/list` и видит все заявки
<img width="752" height="236" alt="Снимок экрана 2026-09-11 210641" src="https://github.com/user-attachments/assets/97da069b-86ca-44e1-9531-5c69189a6f63" />
<img width="483" height="209" alt="Снимок экрана 2026-09-11 210555" src="https://github.com/user-attachments/assets/a185d0e7-6859-4489-92cf-901d9326ed9a" />
<img width="762" height="357" alt="Снимок экрана 2026-09-11 210621" src="https://github.com/user-attachments/assets/8e958a86-1099-47a5-8e2c-ee21d612b9b7" />
<img width="437" height="333" alt="Снимок экрана 2026-09-11 210521" src="https://github.com/user-attachments/assets/9e9e8502-4a95-41bc-a493-35181ce648d3" />
<img width="744" height="276" alt="Снимок экрана 2026-09-11 210450" src="https://github.com/user-attachments/assets/67791eb2-5e77-4bd1-a776-ebb3f08613c7" />


