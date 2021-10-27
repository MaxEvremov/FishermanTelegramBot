from aiogram import types, Dispatcher
from create_Fisherman import bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного общения', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом в ЛС, пожалуйста напишите ему: '
                            '\nhttps://t.me/Fisherman_from_YekaterinburgBot')


async def fisherman_time(message: types.Message):
    await bot.send_message(message.from_user.id, "24/7 Всегда работаем")


async def fisherman_place(message: types.Message):
    await bot.send_message(message.from_user.id, "У Эдика дома")


async def price_list_command(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handles_client(dispatcher: Dispatcher):
    dispatcher.register_message_handler(command_start, commands=['start', 'help', 'привет'])
    dispatcher.register_message_handler(fisherman_time, commands=['Режим_работы'])
    dispatcher.register_message_handler(fisherman_place, commands=['Расположение'])
    dispatcher.register_message_handler(price_list_command, commands=['Прайс-лист'])
