import sqlite3 as sq
from create_Fisherman import bot


def sql_start():
    global base, cur
    base = sq.connect('fish_cool.db')
    cur = base.cursor()
    if base:
        print('Database connect OK!')
    base.execute('CREATE TABLE IF NOT EXISTS list(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO list VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM list').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
