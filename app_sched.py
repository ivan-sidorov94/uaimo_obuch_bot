import aioschedule
import asyncio
import pendulum
from datetime import datetime
from data_base import sqlite_db
from create_bot import bot
from dotenv import load_dotenv
import os

load_dotenv('/data/stack.env')

chat_id = os.environ.get('chat_id')
ksu_id = os.environ.get('ksu_id')

dict1 = ['OT', 'PB', 'EB', 'PJB', 'OPMB', 'PJB1', 'MED_OSM']
dict2 = ['Проверка знаний по Охране Труда', 'Проверка знаний по Промышленной Безопасности', 'Проверка знаний по Электробезопасности', 'Обучение по Пожарной Безопасности', 'Обучение по Оказанию Первой Медицинской Помощи', 'Обучение по Пожарной Безопасности', 'Медецинский осмотр']
text3 = ''


async def scheduler():
    aioschedule.every(1).day.at("09:00").do(schedule)
    # aioschedule.every(1).day.at("09:00").do(date_ot)
    # aioschedule.every(1).day.at("09:00").do(date_pb)
    # aioschedule.every(1).day.at("09:00").do(date_eb)
    # aioschedule.every(1).day.at("09:00").do(date_pjb)
    # aioschedule.every(1).day.at("09:00").do(date_opmb)
    # aioschedule.every(1).day.at("09:00").do(date_med_osm)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def schedule():
    date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
    current_date = datetime.now().strftime('%m')
    for i, x in zip(dict1, dict2):
        try:
            if date == ''.join(sqlite_db.cur.execute(f"SELECT {i} FROM users WHERE {i}= ?", (date,)).fetchone()):
                print('gotcha!')
                users_id1 = sqlite_db.cur.execute(f"SELECT user_id FROM users WHERE {i} = ?", (date,)).fetchall()
                users_lastname_list = ', '.join(row[0] for row in sqlite_db.cur.execute(f"SELECT user_lastname FROM users WHERE {i} = ?", (date,)).fetchall())
                text1 = (date + f' У Вас {x}'+'.')
                text2 = (date + f' {x} у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
                for row in users_id1:
                    await bot.send_message(row[0], text1)
                    await asyncio.sleep(0.5)
                await asyncio.sleep(1)
                await bot.send_message(chat_id, text=text2)
        except Exception as e:
            pass
        users_id2 = sqlite_db.cur.execute(f"SELECT user_id FROM users WHERE {i} LIKE ?", (f'%.{current_date}.%',)).fetchall()
        if not users_id2:
            continue
        users_lastname_list = ', '.join(row[0] for row in cur.execute(f"SELECT user_lastname FROM users WHERE {i} LIKE ?", (f'%{current_date}.%',)).fetchall())
        text3 = text3 + f'{x} у следующих работников:\n{users_lastname_list}.\n'
        for row in users_id2:
            await bot.send_message(ksu_id, text3)


# async def date_ot():
#     date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
#     try:
#         if date == ''.join(sqlite_db.cur.execute("SELECT OT FROM users WHERE OT = ?", (date,)).fetchone()):
#             users_id = sqlite_db.cur.execute("SELECT user_id FROM users WHERE OT = ?", (date,)).fetchall()
#             users_lastname_list = ', '.join(row[0] for row in sqlite_db.cur.execute("SELECT user_lastname FROM users WHERE OT = ?", (date,)).fetchall())
#             text1 = (date + ' У Вас проверка знаний по Охране Труда')
#             text2 = (date + ' Проверка знаний по Охране Труда у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
#             for row in users_id:
#                 await bot.send_message(row[0], text1)
#                 await asyncio.sleep(0.5)
#             await asyncio.sleep(1)
#             await bot.send_message(chat_id, text=text2)
#     except Exception as e:
#         print(e)
#         pass


# async def date_pb():
#     date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
#     try:
#         if date == ''.join(sqlite_db.cur.execute("SELECT PB FROM users WHERE PB = ?", (date,)).fetchone()):
#             users_id = sqlite_db.cur.execute("SELECT user_id FROM users WHERE PB = ?", (date,)).fetchall()
#             users_lastname_list = ', '.join(row[0] for row in sqlite_db.cur.execute("SELECT user_lastname FROM users WHERE PB = ?", (date,)).fetchall())
#             text1 = (date + ' У Вас проверка знаний по Промышленной Безопасности')
#             text2 = (date + ' Проверка знаний по Промышленной Безопасности у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
#             for row in users_id:
#                 await bot.send_message(row[0], text1)
#                 await asyncio.sleep(0.5)
#             await asyncio.sleep(1)
#             await bot.send_message(chat_id, text=text2)
#     except Exception as e:
#         print(e)
#         pass


# async def date_eb():
#     date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
#     try:
#         if date == ''.join(sqlite_db.cur.execute("SELECT EB FROM users WHERE EB = ?", (date,)).fetchone()):
#             users_id = sqlite_db.cur.execute("SELECT user_id FROM users WHERE EB = ?", (date,)).fetchall()
#             users_lastname_list = ', '.join(row[0] for row in sqlite_db.cur.execute("SELECT user_lastname FROM users WHERE EB = ?", (date,)).fetchall())
#             text1 = (date + ' У Вас проверка знаний по Электробезопасности')
#             text2 = (date + ' Проверка знаний по Электробезопасности у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
#             for row in users_id:
#                 await bot.send_message(row[0], text1)
#                 await asyncio.sleep(0.5)
#             await asyncio.sleep(1)
#             await bot.send_message(chat_id, text=text2)
#     except Exception as e:
#         print(e)
#         pass


# async def date_pjb():
#     date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
#     try:
#         if date == ''.join(sqlite_db.cur.execute("SELECT PJB FROM users WHERE PJB = ?", (date,)).fetchone()):
#             users_id = sqlite_db.cur.execute("SELECT user_id FROM users WHERE PJB = ?", (date,)).fetchall()
#             users_lastname_list = ', '.join(row[0] for row in sqlite_db.cur.execute("SELECT user_lastname FROM users WHERE PJB = ?", (date,)).fetchall())
#             text1 = (date + ' У Вас обучение по Пожарной Безопасности')
#             text2 = (date + ' Обучение по Пожарной Безопасности у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
#             for row in users_id:
#                 await bot.send_message(row[0], text1)
#                 await asyncio.sleep(0.5)
#             await asyncio.sleep(1)
#             await bot.send_message(chat_id, text=text2)
#     except Exception as e:
#         print(e)
#         pass

#     try:
#         if date == ''.join(sqlite_db.cur.execute("SELECT PJB1 FROM users WHERE PJB1 = ?", (date,)).fetchone()):
#             users_id = sqlite_db.cur.execute("SELECT user_id FROM users WHERE PJB1 = ?", (date,)).fetchall()
#             users_lastname_list = ', '.join(row[0] for row in sqlite_db.cur.execute("SELECT user_lastname FROM users WHERE PJB1 = ?", (date,)).fetchall())
#             text1 = (date + ' У Вас обучение по Пожарной Безопасности')
#             text2 = (date + ' Обучение по Пожарной Безопасности у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
#             for row in users_id:
#                 await bot.send_message(row[0], text1)
#                 await asyncio.sleep(0.5)
#             await asyncio.sleep(1)
#             await bot.send_message(chat_id, text=text2)
#     except Exception as e:
#         print(e)
#         pass


# async def date_opmb():
#     date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
#     try:
#         if date == ''.join(sqlite_db.cur.execute("SELECT OPMB FROM users WHERE OPMB = ?", (date,)).fetchone()):
#             users_id = sqlite_db.cur.execute("SELECT user_id FROM users WHERE OPMB = ?", (date,)).fetchall()
#             users_lastname_list = ', '.join(row[0] for row in sqlite_db.cur.execute("SELECT user_lastname FROM users WHERE OPMB = ?", (date,)).fetchall())
#             text1 = (date + ' У Вас обучение по Оказанию Первой Медицинской Помощи')
#             text2 = (date + ' Обучение по Оказанию Первой Медицинской Помощи у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
#             for row in users_id:
#                 await bot.send_message(row[0], text1)
#                 await asyncio.sleep(0.5)
#             await asyncio.sleep(1)
#             await bot.send_message(chat_id, text=text2)
#     except Exception as e:
#         print(e)
#         pass


# async def date_med_osm():
#     date = str(pendulum.today().add(days=3).format("DD.MM.YYYY"))
#     try:
#         if date == ''.join(sqlite_db.cur.execute("SELECT MED_OSM FROM users WHERE MED_OSM = ?", (date,)).fetchone()):
#             users_id = sqlite_db.cur.execute("SELECT user_id FROM users WHERE MED_OSM = ?", (date,)).fetchall()
#             users_lastname_list = ', '.join(row[0] for row in sqlite_db.cur.execute("SELECT user_lastname FROM users WHERE MED_OSM = ?", (date,)).fetchall())
#             text1 = (date + ' У Вас Медецинский осмотр')
#             text2 = (date + ' Медецинский осмотр у следующих работников:\n'+ users_lastname_list + '. \nПосле ознакомления ставим лайк.')
#             for row in users_id:
#                 await bot.send_message(row[0], text1)
#                 await asyncio.sleep(0.5)
#             await asyncio.sleep(1)
#             await bot.send_message(chat_id, text=text2)
#     except Exception as e:
#         print(e)
#         pass


def register_scheduler():
   asyncio.create_task(scheduler())