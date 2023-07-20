from aiogram.utils import executor
from create_bot import dp 
from data_base import sqlite_db
import app_sched
import os


async def on_startup(_):
    app_sched.register_scheduler()
    await sqlite_db.sql_start()
    print(os.environ.get('admin_id'))

executor.start_polling(dp, skip_updates=False, on_startup=on_startup)