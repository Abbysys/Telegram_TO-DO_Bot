from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from loader import dp


# Вызывает справку
@dp.message_handler(Text(equals=['/help', 'Помощь']))
async def bot_help(message: types.Message):
    text = [
        'Хей! Вот полный список доступных команд:\n',
        '/help - Показать все команды',
        '/new_item "название задачи" - добавить новую задачу',
        '/delete "номер задачи" - удалить задачу с заданным номером',
        '/all - посмотреть список задач в формате',
        '/keyboard - показать клавиатуру',
        '/remove_keyboard - убрать клавиатуру'
        '/start - идентификация пользователя'
    ]  # записываем в обычный список, а потом с помощью join выводим каждое предложение с новой строки
    await message.answer('\n'.join(text))
