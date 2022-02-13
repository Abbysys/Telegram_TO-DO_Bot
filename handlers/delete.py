from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text
from loader import dp
from states import WatchForArgs


# Функция, которая работает непосредственно с txt файлом и удаляет задачу, сохраняя при этом
# правильную нумерацию
def delete_task(message):
    if message.get_args() is None:
        num = message.text
    else:
        num = message.get_args()
    name = message.from_user.full_name
    user_info_path = rf'Users_Data\{name}.txt'
    with open(user_info_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    if not num.isdigit() or int(num) > int(data[0]) or int(num) <= 0:
        return 'out of range'
    current_num_tasks = int(data[0]) - 1
    data[0] = f'{current_num_tasks}\n'
    new_data = data[:int(num)]
    if new_data is []:
        new_data.append(str(0))
    if (current_num_tasks + 1) != num and current_num_tasks != 0:

        for i in range(int(num) + 1, len(data)):
            old_text = data[i]
            new_text = old_text.replace(str(i), str(i - 1), 1)
            new_data.append(new_text)

    with open(user_info_path, 'w', encoding='utf-8') as file:
        for elem in new_data:
            file.write(elem)
    return 'ok'


# Функция, которая возвращает строку - ответ пользователю для message.answer()
def answer_on_del(message):
    name = message.from_user.full_name
    user_info_path = rf'Users_Data\{name}.txt'
    with open(user_info_path, 'r', encoding='utf-8') as file:
        tasks_left = file.readline()
    if tasks_left.strip() == str(0):
        return 'Молодец! Все задачи выполнены!'
    else:
        return f'Еще одна задача выполнена! Так держать!\n\nЗадач осталось: {tasks_left.strip()}'


# Хендлер для чтение команды. Он же определяет, с аргументом ли сообщение (/delete 3), или
# пользователь предпочел написать аргкмент отдельным сообщением
@dp.message_handler(Text(equals=['/delete', 'Удалить задачу']))
async def delete(message: types.Message):
    args = message.get_args()
    if args:  # Как раз таки проверка на наличие аргумента
        result = delete_task(message)
        if result != 'ok':
            await message.answer(text='Нет задачи с таким номером\n\nЧтобы посмотреть текущий список задач, '
                                      'воспользуйтесь командой /all')
            return
        answer = answer_on_del(message)
        await message.answer(text=answer)

    else:
        await message.answer('Введи номер выполненной задачи: ')
        await WatchForArgs.without_arg_del.set()


# Хендлер, который будет ловить аргументы (номера задачи) для удаления
# Чтобы в него попасть, должно быть состояние WatchForArgs.without_arg_del
@dp.message_handler(state=WatchForArgs.without_arg_del, content_types=types.ContentTypes.TEXT)
async def delete_state(message: types.Message, state: FSMContext):
    result = delete_task(message)
    if result != 'ok':
        await message.answer(text='Нет задачи с таким номером\n\nЧтобы посмотреть текущий список задач, '
                                  'воспользуйтесь командой /all')
        await state.finish()
    else:
        answer = answer_on_del(message)
        await message.answer(text=answer)
        await state.finish()
