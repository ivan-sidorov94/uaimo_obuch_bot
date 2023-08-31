import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils.exceptions import ChatNotFound, BotBlocked
from data_base.sqlite_db import DBManager
from dotenv import load_dotenv
import os
import asyncio

load_dotenv('./data/stack.env')

TOKEN=os.environ.get('TOKEN')
admin_id = os.environ.get('admin_id')

async def db_start():
    global db
    db = DBManager()
    await db.start()
    

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher(bot)


# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    but = [
        types.InlineKeyboardButton(text="Узнать дату обучения", callback_data="obuch"),
        #types.InlineKeyboardButton(text="ПБ", callback_data="ПБ"),
        #types.InlineKeyboardButton(text="ЭБ", callback_data="ЭБ"),
        #types.InlineKeyboardButton(text="ПожБ", callback_data="ПожБ"),
        #types.InlineKeyboardButton(text="ОПМБ", callback_data="ОПМБ"),
        
    ]
    but1 = [
        types.InlineKeyboardButton(text="Узнать дату медицинского осмотра", callback_data="med_osm")
    ]


    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(*but)
    keyboard.row(*but1)
    if not await db.user_exists(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await bot.send_message(message.from_user.id, "Здесь Вы можете узнать дату обучения по ОТ, ПБ, ЭБ, ПожБ, ОПМБ и дату Медицинского осмотра", reply_markup=keyboard)
    else:
        await bot.send_message(message.from_user.id,"Здесь Вы можете узнать дату обучения по ОТ, ПБ, ЭБ, ПожБ, ОПМБ и дату Медицинского осмотра", reply_markup=keyboard)
    

        

# Хендлер на команду /send
@dp.message_handler(commands="send")
async def send_message(message: types.Message):
    if message.from_user.id != admin_id:
        await bot.send_message(message.from_user.id, "Вы не являетесь Администратором")
        return
    message_text = message.text.split('/send ')[1]
    try:
        for users in await db.get_all_users():
            try:
                await bot.send_message(int(users), message_text)
                await asyncio.sleep(0.5)
            except ChatNotFound:
                print(f"Chat not found for user {users}. Ignoring error.")
                pass
            except BotBlocked:
                print(f"Chat was blocked for user {users}. Ignoring error.")
                pass
        await bot.send_message(admin_id, 'Рассылка завершена')
    except Exception as e:
        print(f"An error occured: {e}")
        pass


@dp.callback_query_handler(text="ОТ")
async def ot(call: types.CallbackQuery):
    try:
        date_ot = ''.join(await db.get_date_ot(call.from_user.id))
        await call.message.answer("Проверка знаний по Охране Труда: "+ date_ot)
        await call.answer()
    except:
        await call.message.answer("У Вас нет проверки знаний по Охране Труда")
        await call.answer()
        await db.base.commit()

@dp.callback_query_handler(text="ПБ")
async def ot(call: types.CallbackQuery):
    try:
        date_pb = ''.join(await db.get_date_pb(call.from_user.id))
        await call.message.answer("Проверка знаний по Промышленной Безопасности: "+ date_pb)
        await call.answer()
    except:
        await call.message.answer("У Вас нет проверки знаний по Промышленной Безопасности")
        await call.answer()
        await db.base.commit()

@dp.callback_query_handler(text="ЭБ")
async def ot(call: types.CallbackQuery):
    try:
        date_eb = ''.join(await db.get_date_eb(call.from_user.id))
        await call.message.answer("Проверка знаний по Электробезопасности: "+ date_eb)
        await call.answer()
    except:
        await call.message.answer("У Вас нет проверки знаний по Электробезопасности")
        await call.answer()
        await db.base.commit()

@dp.callback_query_handler(text="ПожБ")
async def ot(call: types.CallbackQuery):
    try:
        date_pjb = ''.join(await db.get_date_pjb(call.from_user.id))
        date_pjb1 = ''.join(await db.get_date_pjb1(call.from_user.id))
        await call.message.answer("Проверки знаний по Пожарной Безопасности: "+ date_pjb + " и " + date_pjb1)
        await call.answer()
    except:
        await call.message.answer("У Вас нет проверок знаний по Пожарной Безопасности")
        await call.answer()
        await db.base.commit()

@dp.callback_query_handler(text="ОПМБ")
async def ot(call: types.CallbackQuery):
    try:
        date_opmb = ''.join(await db.get_date_opmb(call.from_user.id))
        await call.message.answer("Проверка знаний по Оказанию Первой Медицинской Помощи: "+ date_opmb)
        await call.answer()
    except:
        await call.message.answer("У Вас нет проверки знаний по Оказанию Первой Медицинской Помощи")
        await call.answer()
        await db.base.commit()

@dp.callback_query_handler(text="obuch")
async def obuch(call: types.CallbackQuery):
    try:
        date_ot = ''.join(await db.get_date_ot(call.from_user.id))
        await call.message.answer("Проверка знаний по Охране Труда: "+ date_ot)
        await call.answer()
    except:
        pass
    try:
        date_pb = ''.join(await db.get_date_pb(call.from_user.id))
        await call.message.answer("Проверка знаний по Промышленной Безопасности: "+ date_pb)
        await call.answer()
    except:
        pass
    try:
        date_eb = ''.join(await db.get_date_eb(call.from_user.id))
        await call.message.answer("Проверка знаний по Электробезопасности: "+ date_eb)
        await call.answer()
    except:
        pass
    try:
        date_pjb = ''.join(await db.get_date_pjb(call.from_user.id))
        date_pjb1 = ''.join(await db.get_date_pjb1(call.from_user.id))
        await call.message.answer("Проверки знаний по Пожарной Безопасности: "+ date_pjb + " и " + date_pjb1)
        await call.answer()
    except:
        pass
    try:
        date_opmb = ''.join(await db.get_date_opmb(call.from_user.id))
        await call.message.answer("Проверка знаний по Оказанию Первой Медицинской Помощи: "+ date_opmb)
        await call.answer()
    except:
        pass
    await db.base.commit()

@dp.callback_query_handler(text="med_osm")
async def ot(call: types.CallbackQuery):
    try:
        date_med_osm = ''.join(await db.get_date_med_osm(call.from_user.id))
        await call.message.answer("Дата медецинского осмотра: "+ date_med_osm)
        await call.answer()
    except:
        await call.message.answer("У Вас нет медецинского осмотра")
        await call.answer()

