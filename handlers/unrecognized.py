from aiogram import types
from loader import dp


# Сюда попадает все непонятное
@dp.message_handler(content_types=types.ContentTypes.ANY)
async def bot_help(message: types.Message):
    text = ['Извини, я тебя не понимаю :(\n',
            'Чтобы узнать доступные команды, используй /help']
    await message.answer('\n'.join(text))
