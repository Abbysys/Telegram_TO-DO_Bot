from aiogram import types
from aiogram import executor
from handlers import dp

# Запуск бота здесь
# Bot: @todo_project_bot
# ник: TODO_SPbU


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('help', 'Получить справку в сообщении'),
        types.BotCommand('new_item', 'Создать новую задачу'),
        types.BotCommand('delete', 'Удалить выбранную задачу'),
        types.BotCommand('all', 'Просмотреть все задачи'),
        types.BotCommand('keyboard', 'Показать клавиатуру'),
        types.BotCommand('remove_keyboard', 'Убрать клавиатуру'),
        types.BotCommand('start', 'Идентификация пользователя'),
    ])
executor.start_polling(dp, on_startup=set_default_commands)


