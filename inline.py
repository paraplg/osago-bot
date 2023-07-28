from aiogram import types


async def start_inline_btn():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('💳 Пополнить баланс', callback_data='profile:addbalance'),
        types.InlineKeyboardButton('🧰 История заказов (0)', callback_data='profile:history'),
    )
    return btn


async def balance_inline_btn():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('💸 Оплатить', callback_data='balance:pay'),
        types.InlineKeyboardButton('❌ Отменить', callback_data='balance:back'),
    )
    return btn


async def products_inline_btn():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('📑Купить ОСАГО', callback_data='products:osago'),
        types.InlineKeyboardButton('📋Техосмотр', callback_data='products:inspection'),
        types.InlineKeyboardButton('📸Фотошоп техосмотр', callback_data='products:photoshop'),
        types.InlineKeyboardButton('🏦КАСКО для банка', callback_data='products:casco'),
        types.InlineKeyboardButton('🏪Карта учета ГИБДД', callback_data='products:GIBDD'),
        types.InlineKeyboardButton('🚓Карта ВУ по базе ГАИ', callback_data='products:GAI'),  
        types.InlineKeyboardButton('🔎Поиск по базе Солярис', callback_data='products:find'),  
        types.InlineKeyboardButton('🏦Для восстановления КБМ', callback_data='products:KBM'),  
        types.InlineKeyboardButton('🏷Договор купли продажи', callback_data='products:sellbuy'),  
        types.InlineKeyboardButton('📇Снятие ТС с учета', callback_data='products:TS')  
    )
    return btn


async def osago():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Е-осаго на год | 1900руб.', callback_data='products:osago1'),
        types.InlineKeyboardButton('Е-осаго на 3 мес | 1600руб.', callback_data='products:osago2'),
        types.InlineKeyboardButton('Осаго для учета однодневка | 1500руб.', callback_data='products:osago3'),
        types.InlineKeyboardButton('Е-осаго без базы | 1900руб.', callback_data='products:osago4'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='products:back'),
    )
    return btn
async def inspection():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Диагностическая карта B | 3000руб.', callback_data='products:inspection1'),
        types.InlineKeyboardButton('Диагностическая карта C | 4300руб.', callback_data='products:inspection2'),
        types.InlineKeyboardButton('Диагностическая карта без базы 1 год | 500руб.', callback_data='products:inspection3'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='products:back'),
    )
    return btn
async def photoshop():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Фотошоп техосмотр | 250руб.', callback_data='products:photoshop1'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='products:back'),
    )
    return btn
async def casco():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('КАСКО для банка | 5000руб.', callback_data='products:casco1'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='products:back'),
    )
    return btn
async def GIBDD():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Карта учета ГИБДД | 1000руб.', callback_data='products:GIBDD1'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='products:back'),
    )
    return btn
async def GAI():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('ВУ по базе ГАИ | 1000руб.', callback_data='products:GAI1'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='products:back'),
    )
    return btn
async def find():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Поиск по базе Солярис | 1000руб.', callback_data='products:find1'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='products:back'),
    )
    return btn
async def KBM():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('1.17 (с ДТП) | 6000руб.', callback_data='products:KBM1'),
        types.InlineKeyboardButton('2.25 | 7500руб.', callback_data='products:KBM2'),
        types.InlineKeyboardButton('1.76 | 7000руб.', callback_data='products:KBM3'),
        types.InlineKeyboardButton('1.17 (без ДТП) | 5000руб.', callback_data='products:KBM4'),
        types.InlineKeyboardButton('2.94 | 7500руб.', callback_data='products:KBM5'),
        types.InlineKeyboardButton('3.92 | 8000руб.', callback_data='products:KBM6'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='products:back'),
    )
    return btn
async def sellbuy():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Договор купли продажи | 500руб.', callback_data='products:sellbuy1'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='products:back'),
    )
    return btn
async def TS():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Снятие ТС с учета | 8000руб.', callback_data='products:TS1'),
        types.InlineKeyboardButton('🔙 Назад', callback_data='products:back'),
    )
    return btn