from aiogram import types
from loader import dp
from aiogram.dispatcher.filters.builtin import Text


# Показывает все актуальные задачи пользователя

@dp.message_handler(Text(equals=['/all', 'Показать все задачи']))
async def show_all(message: types.Message):
    name = message.from_user.full_name
    user_info_path = rf'Users_Data\{name}.txt'
    with open(user_info_path, 'r', encoding='utf-8') as file:
        arg = file.readline()  # чтобы пропустить первую строку, где хранится число задач
        data = file.read()
    await message.answer(f'Вот список всех твоих задач:\n\n{data}')
