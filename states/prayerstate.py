from aiogram.dispatcher.filters.state import State, StatesGroup

# Namoz o'qish uchun `State`
class Prayer(StatesGroup):
    maintype = State()
    subtype = State()
    videotype = State()
    timetype = State()


# Reklama yuborish uchun `State`
class Suratli(StatesGroup):
    textli = State()
    suratli = State()

class Textli(StatesGroup):
    textli = State()

class Videoli(StatesGroup):
    textli = State()
    videoli = State()


# Fikr uchun `State`
class Fikr(StatesGroup):
    fikr = State()


# Quron uchun `State`
class Quran(StatesGroup):
    chapter = State()
    verse = State()