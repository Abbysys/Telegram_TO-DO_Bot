from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
import os


# Хендлер при запуске бота пользователем. Создает новый файл txt с именем, соответсвующим имени пользователя
@dp.message_handler(CommandStart())
async def bot_starting(message: types.Message):
    name = message.from_user.full_name
    greet = 'Привет, ' + str(name) + '!'
    user_info_path = rf'Users_Data\{name}.txt'
    if not os.path.exists(user_info_path):
        with open(user_info_path, 'w') as file:
            file.write('0\n')
    await message.answer(text=greet)

