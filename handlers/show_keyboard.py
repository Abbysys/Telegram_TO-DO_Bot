from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import Text

from loader import dp
from keyboard import keybd


# Показывает клавиатуру
@dp.message_handler(Command('keyboard'))
async def show_keyboard(message: types.Message):
    await message.answer('Выберите одну из команд', reply_markup=keybd)


# Удаляет клавиатуру
@dp.message_handler(Text(equals=['/remove_keyboard', 'Убрать клавиатуру']))
async def show_keyboard(message: types.Message):
    await message.answer('Клавиатура убрана', reply_markup=ReplyKeyboardRemove())
