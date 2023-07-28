from aiogram import types


async def start_btn():
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row('📂 Наши услуги', '👤 Профиль')
    btn.row('☎️ Обратная связь', '💥Телеграм канал')
    return btn