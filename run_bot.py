from aiogram.utils import executor
from create_bot import dp, db_start
import app_sched

async def on_startup(_):
    app_sched.register_scheduler()
    await db_start()   

executor.start_polling(dp, skip_updates=False, on_startup=on_startup)