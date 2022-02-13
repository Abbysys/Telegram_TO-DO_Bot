from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# тут файл подгрузок. Отсюда я брал диспатчер в другие файлы(конкретно в хэндлеры),
# память для машины состояний, присвоил боту токен

bot_token = 'Тут введите токен бота'
bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


