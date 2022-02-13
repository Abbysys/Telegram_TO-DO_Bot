from aiogram.dispatcher.filters.state import StatesGroup, State


# Здесь хранятся состояния из FSM

class WatchForArgs(StatesGroup):
    without_arg_new = State()
    without_arg_del = State()
    out_of_tasks = State()
