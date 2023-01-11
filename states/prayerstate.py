from aiogram.dispatcher.filters.state import State, StatesGroup


class Prayer(StatesGroup):
    maintype = State()
    subtype = State()
    videotype = State()
    timetype = State()

class Suratli(StatesGroup):
    textli = State()
    suratli = State()

class Textli(StatesGroup):
    textli = State()

class Videoli(StatesGroup):
    textli = State()
    videoli = State()

class Fikr(StatesGroup):
    fikr = State()