from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Прайс-лист')
b4 = KeyboardButton('Поделиться номером, для того,\n чтобы мы связались с вами', request_contact=True)
b5 = KeyboardButton('Отправьте своё местоположение\n для доставки', request_location=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True,)

kb_client.row(b1, b2, b3).add(b4, b5)