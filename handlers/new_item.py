from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import Text
from loader import dp
from states import WatchForArgs


# Функция, которая работает с txt файлом и добавляет новую задачу, сохраняя при этом правильную нумерацию
def new_item(message):
    if message.get_args() is None:
        task = message.text
    else:
        task = message.get_args()
    name = message.from_user.full_name
    user_info_path = rf'Users_Data\{name}.txt'
    with open(user_info_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    current_num_tasks = int(data[0]) + 1
    data[0] = f'{current_num_tasks}\n'
    with open(user_info_path, 'w', encoding='utf-8') as file:
        # сначала записываем в файл старые записи (Такая перезапись нужна, чтобы хранить актуальное
        # количество введенных задач)
        for elem in data:
            file.write(elem)
        # Тут запись новой задачи
        file.write(f'{current_num_tasks}) {task}\n')


# Ловит команды для добавления задачи
@dp.message_handler(Text(equals=['/new_item', 'Добавить задачу']))
async def create_new_item(message: types.Message):
    args = message.get_args()
    if args:
        new_item(message)
        await message.answer(f'Записана следующая задача:\n\n{args}')
    else:
        await message.answer('Введи задачу: ')
        await WatchForArgs.without_arg_new.set()


# Хендлер, который будет ловить аргументы (Задача) для добавления новой заметки
# Чтобы в него попасть, должно быть состояние WatchForArgs.without_arg_new
@dp.message_handler(state=WatchForArgs.without_arg_new, content_types=types.ContentTypes.TEXT)
async def create_new_item(message: types.Message, state: FSMContext):
    new_item(message)
    text = message.text
    await message.answer(f'Записана следующая задача:\n\n{text}')
    await state.finish()
