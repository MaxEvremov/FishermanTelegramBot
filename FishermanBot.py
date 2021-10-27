from aiogram.utils import executor
from create_Fisherman import dp
from handlers import client, admin, other
from data_base import sqlite_db

async def on_startup(_):
    print('Бот вышел онлайн')
    sqlite_db.sql_start()

client.register_handles_client(dp)
admin.register_handlers_admin(dp)
other.register_handles_other(dp)


executor.start_polling(dp, skip_updates=False, on_startup=on_startup)

