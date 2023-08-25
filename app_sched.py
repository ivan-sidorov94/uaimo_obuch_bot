import aioschedule
import asyncio
import pendulum
from data_base.sqlite_db import DBManager
from create_bot import bot
from dotenv import load_dotenv
import os

load_dotenv('./data/.env')

chat_id = os.environ.get('chat_id')
ksu_id = os.environ.get('ksu_id')


db = DBManager()

async def scheduler():
    aioschedule.every(1).day.at("09:00").do(date_ot)
    aioschedule.every(1).day.at("09:00").do(date_pb)
    aioschedule.every(1).day.at("09:00").do(date_eb)
    aioschedule.every(1).day.at("09:00").do(date_pjb)
    aioschedule.every(1).day.at("09:00").do(date_opmb)
    aioschedule.every(1).day.at("09:00").do(date_med_osm)
    aioschedule.every(1).day.at("09:00").do(monthly)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def date_ot():
    date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
    try:
        if date == ''.join(await (await db.cur.execute("SELECT OT FROM users WHERE OT = ?", (date,))).fetchone()):
            users_id = await (await db.cur.execute("SELECT user_id FROM users WHERE OT = ?", (date,))).fetchall()
            users_lastname_list = ', '.join(row[0] for row in await (await db.cur.execute("SELECT user_lastname FROM users WHERE OT = ?", (date,))).fetchall())
            text1 = (date + ' У Вас обучение по Охране Труда')
            text2 = (date + ' Обучение по Охране Труда у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
            for row in users_id:
                await bot.send_message(row[0], text1)
                await asyncio.sleep(0.5)
            await asyncio.sleep(1)
            await bot.send_message(chat_id, text=text2)
    except Exception as e:
        pass
    await db.base.commit() 

async def date_pb():
    date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
    try:
        if date == ''.join(await (await db.cur.execute("SELECT PB FROM users WHERE PB = ?", (date,))).fetchone()):
            users_id = await (await db.cur.execute("SELECT user_id FROM users WHERE PB = ?", (date,))).fetchall()
            users_lastname_list = ', '.join(row[0] for row in await (await db.cur.execute("SELECT user_lastname FROM users WHERE PB = ?", (date,))).fetchall())
            text1 = (date + ' У Вас обучение по Промышленной Безопасности')
            text2 = (date + ' Обучение по Промышленной Безопасности у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
            for row in users_id:
                await bot.send_message(row[0], text1)
                await asyncio.sleep(0.5)
            await asyncio.sleep(1)            
            await bot.send_message(chat_id, text=text2)
    except Exception as e:
        pass
    await db.base.commit()

async def date_eb():
    date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
    try:
        if date == ''.join(await (await db.cur.execute("SELECT EB FROM users WHERE EB = ?", (date,))).fetchone()):
            users_id = await (await db.cur.execute("SELECT user_id FROM users WHERE EB = ?", (date,))).fetchall()
            users_lastname_list = ', '.join(row[0] for row in await (await db.cur.execute("SELECT user_lastname FROM users WHERE EB = ?", (date,))).fetchall())
            text1 = (date + ' У Вас обучение по Электробезопасности')
            text2 = (date + ' Обучение по Электробезопасности у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
            for row in users_id:
                await bot.send_message(row[0], text1)
                await asyncio.sleep(0.5)
            await asyncio.sleep(1)            
            await bot.send_message(chat_id, text=text2)
    except Exception as e:
        pass 
    await db.base.commit()

async def date_pjb():
    date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
    try:
        if date == ''.join(await (await db.cur.execute("SELECT PJB FROM users WHERE PJB = ?", (date,))).fetchone()):
            users_id = await (await db.cur.execute("SELECT user_id FROM users WHERE PJB = ?", (date,))).fetchall()
            users_lastname_list = ', '.join(row[0] for row in await (await db.cur.execute("SELECT user_lastname FROM users WHERE PJB = ?", (date,))).fetchall())
            text1 = (date + ' У Вас обучение по Пожарной Безопасности')
            text2 = (date + ' Обучение по Пожарной Безопасности у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
            for row in users_id:
                await bot.send_message(row[0], text1)
                await asyncio.sleep(0.5)
            await asyncio.sleep(1)            
            await bot.send_message(chat_id, text=text2)
    except Exception as e:
        pass
    try:
        if date == ''.join(await (await db.cur.execute("SELECT PJB1 FROM users WHERE PJB1 = ?", (date,))).fetchone()):
            users_id = await db.cur.execute("SELECT user_id FROM users WHERE PJB1 = ?", (date,)).fetchall()
            users_lastname_list = ', '.join(row[0] for row in await (await db.cur.execute("SELECT user_lastname FROM users WHERE PJB1 = ?", (date,))).fetchall())
            text1 = (date + ' У Вас обучение по Пожарной Безопасности')
            text2 = (date + ' Обучение по Пожарной Безопасности у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
            for row in users_id:
                await bot.send_message(row[0], text1)
                await asyncio.sleep(0.5)
            await asyncio.sleep(1)            
            await bot.send_message(chat_id, text=text2)
    except Exception as e:        
        pass
    await db.base.commit()

async def date_opmb():
    date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
    try:
        if date == ''.join(await (await db.cur.execute("SELECT OPMB FROM users WHERE OPMB = ?", (date,))).fetchone()):
            users_id = await (await db.cur.execute("SELECT user_id FROM users WHERE OPMB = ?", (date,))).fetchall()
            users_lastname_list = ', '.join(row[0] for row in await (await db.cur.execute("SELECT user_lastname FROM users WHERE OPMB = ?", (date,))).fetchall())
            text1 = (date + ' У Вас обучение по Оказанию Первой Медицинской Помощи')
            text2 = (date + ' Обучение по Оказанию Первой Медицинской Помощи у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
            for row in users_id:
                await bot.send_message(row[0], text1)
                await asyncio.sleep(0.5)
            await asyncio.sleep(1)            
            await bot.send_message(chat_id, text=text2)
    except Exception as e:    
        pass
    await db.base.commit()
    
async def date_med_osm():
    date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
    try:
        if date == ''.join(await (await db.cur.execute("SELECT MED_OSM FROM users WHERE MED_OSM = ?", (date,))).fetchone()):
            users_id = await (await db.cur.execute("SELECT user_id FROM users WHERE MED_OSM = ?", (date,))).fetchall()
            users_lastname_list = ', '.join(row[0] for row in await (await db.cur.execute("SELECT user_lastname FROM users WHERE MED_OSM = ?", (date,))).fetchall())
            text1 = (date + ' У Вас Медецинский осмотр')
            text2 = (date + ' Медецинский осмотр у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
            for row in users_id:
                await bot.send_message(row[0], text1)
                await asyncio.sleep(0.5)
            await asyncio.sleep(1)            
            await bot.send_message(chat_id, text=text2)
    except Exception as e:  
        pass 
    await db.base.commit()

async def monthly():
    if pendulum.today().day == 1:
        month = pendulum.today().add(months=1).format('MM')
    try:
        users_list = ', '.join(row[0] for row in await (await db.cur.execute("SELECT user_lastname FROM users WHERE EB LIKE ?", ('%.' + month +'.%',))).fetchall())
        if users_list:
            text1 = ('Обучение по Электробезопасности у следующих работников:\n'+ users_list + '.')
            await bot.send_message(ksu_id, text=text1)
            await asyncio.sleep(0.5)
    except Exception as e:
        pass
    try:
        users_list = ', '.join(row[0] for row in await (await db.cur.execute("SELECT user_lastname FROM users WHERE OT LIKE ?", ('%.' + month +'.%',))).fetchall())
        if users_list:
            text2 = ('Обучение по Охране труда у следующих работников:\n'+ users_list + '.')
            await bot.send_message(ksu_id, text=text2)
            await asyncio.sleep(0.5)
    except Exception as e:
        pass
    try:
        users_list = ', '.join(row[0] for row in await (await db.cur.execute("SELECT user_lastname FROM users WHERE PB LIKE ?", ('%.' + month +'.%',))).fetchall())
        if users_list:
            text3 = ('Обучение по Промышленной безопасности у следующих работников:\n'+ users_list + '.')
            await bot.send_message(ksu_id, text=text3)
            await asyncio.sleep(0.5)
    except Exception as e:
        pass
    pass
    await db.base.commit()


def register_scheduler():
   asyncio.create_task(scheduler())