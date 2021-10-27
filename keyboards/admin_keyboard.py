from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_load = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')
button_cancel = KeyboardButton('отмена')
button_menu = KeyboardButton('меню')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load, button_delete, button_cancel,button_menu)
