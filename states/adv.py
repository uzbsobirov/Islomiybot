from aiogram.dispatcher.filters.state import State, StatesGroup

class Picture(StatesGroup):
    file_id = State()
    text = State()
    choose_yes_no = State()
    choose_yes = State()

class Text(StatesGroup):
    text = State()
    choose_yes_no = State()
    choose_yes = State()

class Video(StatesGroup):
    file_id = State()
    text = State()
    choose_yes_no = State()
    choose_yes = State()