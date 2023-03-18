from aiogram.dispatcher.filters.state import State, StatesGroup

# For `Tolov tarixi`
class PayHistory(StatesGroup):
    channel = State()
    group = State()


# For `Qollanma`
class Manual(StatesGroup):
    text = State()

# For `Admin User`
class AdminUser(StatesGroup):
    username = State()

# For `Minimal summa`
class MinSum(StatesGroup):
    summa = State()


# For `Taklif summa`
class TaklifSumma(StatesGroup):
    summa = State()

# For `Xabar yuborish`
class SendMessage(StatesGroup):
    message = State()

# <----------Majburiy obuna---------->
class AddSponsor(StatesGroup):
    username = State()

class DeleteSponsor(StatesGroup):
    username = State()


from aiogram.dispatcher.filters.state import State, StatesGroup

class Admin(StatesGroup):
    main_admin = State()
    stat = State()
    sending = State()

class SendingGroup(StatesGroup):
    group = State()

class SendingUser(StatesGroup):
    user = State()