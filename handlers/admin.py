from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_Fisherman import bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_keyboard

ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# ПОЛУЧАЕМ ID ТЕКУЩЕГО ПОЛЬЗОВАТЕЛЯ
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что необходимо сделать?', reply_markup=admin_keyboard
                           .button_case_admin)
    await message.delete()


# НАЧИНАЕМ ДИАЛОГ ЗАГРУЗКИ ПРАЙСА
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загружай фото, я сохраняю')


# ЛОВИМ ПЕРВЫЙ ОТВЕТ, и пишем его в словарь
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Теперь вводи название')


# ЛОВИМ ВТОРОЙ ОТВЕТ
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи описание товара')


# ЛОВИМ ТРЕТИЙ ОТВЕТ
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи цену на товар')


# ЛОВИМ ПОСЛЕДНИЙ ОТВЕТ
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
        await sqlite_db.sql_add_command(state)
        await state.finish()


# ВЫХОД ИЗ СОСТОЯНИЙ
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')


# РЕГИСТРИРУЕМ ХЕДЛЕРЫ
def register_handlers_admin(dispatcher: Dispatcher):
    dispatcher.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dispatcher.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dispatcher.register_message_handler(load_name, state=FSMAdmin.name)
    dispatcher.register_message_handler(load_description, state=FSMAdmin.description)
    dispatcher.register_message_handler(load_price, state=FSMAdmin.price)
    dispatcher.register_message_handler(cancel_handler, state="*", commands='отмена')
    dispatcher.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dispatcher.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dispatcher.re
