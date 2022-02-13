from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Тут хранится шаблон клавиатуры

keybd = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Добавить задачу'),
     KeyboardButton(text='Удалить задачу')],
    [KeyboardButton(text='Показать все задачи')],
    [KeyboardButton(text='Помощь'),
     KeyboardButton(text='Убрать клавиатуру')]

], resize_keyboard=True, one_time_keyboard=True
)
