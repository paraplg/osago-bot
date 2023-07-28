import logging
import sqlite3 as sql
from random import randint

from aiogram import Bot, Dispatcher, executor, types
from btn import start_btn
from inline import *
import random

API_TOKEN = '6273084056:AAHxzhlwPOgnFE2usNZd9Pt5_NLSDLh0GKo'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

balance_input_ask = False

global con
global cur
con = sql.connect("my_first_database.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id BIGINT,
        balance BIGINT
        )""")
con.commit()


@dp.message_handler(commands=['start'])
async def start_bot_handler(message: types.Message):
    global balance2
    global user_id
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO users VALUES (?, ?)", (message.from_user.id, 0))
        con.commit()
        balance2 = 0
    else:
        for i in cur.execute(f"SELECT balance FROM users WHERE id = '{message.from_user.id}'"):
            balance2 = i[0]

@dp.message_handler()
async def msg_handler(message: types.Message):
    global how_much
    msg = message.text
    if msg == '📂 Наши услуги':
        products_btn = await products_inline_btn()
        await message.answer('🌐 Наши услуги', reply_markup=products_btn)
    elif msg == '👤 Профиль':
        profile_btn = await start_inline_btn()
        await message.answer(f'👤 Ваш Профиль\n\n🆔 ID: {message.from_user.id}\n💰 Баланс: {balance2} руб.\n\nРеф.ссылка: https://t.me/Osagooa_bot?start={message.from_user.id}', reply_markup=profile_btn)
    elif msg == '☎️ Обратная связь':
        await message.answer('✳️ Гл.Админ бота: @osagomaksc')
    elif msg == '💥Телеграм канал':
        await message.answer('✳️ Наш канал: @osagomak')
    elif balance_input_ask == True:
        how_much = int(msg)
        balance_btn = await balance_inline_btn()
        await message.answer(f'✅ Ссылка для оплаты создан (у вас 15 минут чтобы перевести {msg}руб.)', reply_markup=balance_btn)



@dp.callback_query_handler(text_contains='profile:')
async def profile_choice(call: types.CallbackQuery):
    global balance_input_ask
    choice = call.data.split(':')[1]
    if choice == 'addbalance':
        await call.message.edit_text('✍️ Введите сумму (минимум 100 руб.):')
        balance_input_ask = True

@dp.callback_query_handler(text_contains='balance:')
async def balance_choice(call: types.CallbackQuery):
    global balance2
    choice = call.data.split(':')[1]
    if choice == 'back':
        await call.message.delete()
    elif choice == 'pay':
        balance2 = balance2 + how_much
        cur.execute(f"UPDATE users SET balance = {balance2} WHERE id = {user_id}")
        con.commit()

@dp.callback_query_handler(text_contains='products:')
async def balance_choice(call: types.CallbackQuery):
    choice = call.data.split(':')[1]
    if choice == 'back':
        products_btn = await products_inline_btn()
        await call.message.edit_text('🌐 Наши услуги', reply_markup=products_btn)
    elif choice == 'osago':
        osago_btn = await osago()
        await call.message.edit_text('📑Электронный полис ОСАГО с занесением вашего VIN в базу РСА.\n\nОформим ОСАГО для ЛЮБОГО УЧЕТА.\nБеларусь 🇧🇾 Армения 🇦🇲 Россия 🇷🇺  и тд.\n\nНа любой вид транспорта:\nМотоцикл 🏍 Автомобиль 🚙\nТрактор 🚜  Авто с прицепом 🚗\nГрузовой автомобиль 🚛\nА так же такси 🚕\n\n❗️Все Е-ОСАГО без выплат️ при ДТП\n\n⏳Сроки выполнения заказа от 30 мин до 2х часов при нормальной работе РСА, возможны задержки в зависимости от работы баз ЕАИСТО и РСА\n\nСвой заказ Вы получите по готовности прямо в боте. Мы гарантируем максимально возможную скорость и качество обработки ваших заказов\n\n🎁В качестве бонуса, абсолютно все полисы в бланке будут БЕЗ ОГРАНИЧЕНИЙ НА ИСПОЛЬЗОВАНИЕ ТС', reply_markup=osago_btn)
    elif choice == 'inspection':
        inspection_btn = await inspection()
        await call.message.edit_text('📑Диагностическая карта на любое авто. Оформление Техосмотр для ЮР, ФИЗ лиц и иностранных граждан.\n\nЛюбая категория авто (A, B, C, D, ПРИЦЕП)\n🚖Такси\n🚘Учебная машина\n⚠️Опасные грузы\n\n\n⏳Срок выполнения заказа до 1 часа.', reply_markup=inspection_btn)
    elif choice == 'photoshop':
        photoshop_btn = await photoshop()
        await call.message.edit_text('Уважаемый агенты !\n\n📸 Предоставим услуги фотошоп - для ваших клиентов - на услугу ТЕХОСМОТР  без заезда !\n\nВы присылаете нам фото на улице\n\nМы вам в ответ сделаем качественный фотошоп - и пришлем ваше авто - на пункте ТО !', reply_markup=photoshop_btn)
    elif choice == 'casco':
        casco_btn = await casco()
        await call.message.edit_text('🏦Для оформления полиса.\n\n1)ФИО, дата рож-ния, серия номер паспорта, кем когда выдан, адрес регистрации, конт.номер телефона.\n2)Лица допущенные к управлению( если не без огранич.)ФИО, дата рождения, ВУ, стаж вождения.\n3)По ТС: марка, год выпуска, Vin, птс, гос номер, л.с, рмм.\n4)Наименование банка.\n5)Действительная стоимость автомобиля.\n\n⏳Срок выполнения заказа до 1 часа.', reply_markup=casco_btn)
    elif choice == 'GIBDD':
        GIBDD_btn = await GIBDD()
        await call.message.edit_text('Карта учёта гос. номера', reply_markup=GIBDD_btn)
    elif choice == 'GAI':
        GAI_btn = await GAI()
        await call.message.edit_text('Карта ву фото прав', reply_markup=GAI_btn)
    elif choice == 'find':
        find_btn = await find()
        await call.message.edit_text('Солярис нужные данные: ФИО, ГОД РОЖДЕНИЯ', reply_markup=find_btn)
    elif choice == 'KBM':
        KBM_btn = await KBM()
        await call.message.edit_text('🏦Для восстановления кбм.\n\n1) Нужны фотографии водительского удостоверения с двух сторон.\n2) Для юридических лиц карточка предприятия.\n\n⏳Сроки выполнения заказа от 10 до 15 дней', reply_markup=KBM_btn)
    elif choice == 'sellbuy':
        sellbuy_btn = await sellbuy()
        await call.message.edit_text('🏦Для договор купли продажи.\n\n1) Город\n2) Фио\n3) год рождения\n4) паспорт данные покупателя и продавца прописки\n5) данные авто стс либо птс\n6) сумма продажи авто числа\n\n⏳Сроки выполнения заказа от 5 до 10 минут', reply_markup=sellbuy_btn)
    elif choice == 'TS':
        TS_btn = await TS()
        await call.message.edit_text('🏦Для снятие ТС с учета.\n\n1) Паспорт собственника\n2) прописка\n3) птс стс 2 сторон\n4) паспорт того кто ее купил так же лицевая\n⏳Сроки выполнения заказа от 2 до 8 часов', reply_markup=TS_btn)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)