import json
import os
import string

from aiogram import types, Dispatcher, Bot

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('D:/TelegramBotFisherman/cenz.json')))) != set():
        await message.reply('Мат запрещён!')
        await message.delete()


def register_handles_other(dp1: Dispatcher):
    dp1.register_message_handler(echo_send)

