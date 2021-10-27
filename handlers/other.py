import json
import string
from aiogram import types, Dispatcher


async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('D:/TelegramBotFisherman/cenz.json')))) != set():
        await message.reply('Мат запрещён!')
        await message.delete()


def register_handles_other(dispatcher: Dispatcher):
    dispatcher.register_message_handler(echo_send)
