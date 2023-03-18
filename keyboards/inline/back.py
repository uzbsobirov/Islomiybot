from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Orqaga qaytish uchun umumiy knopka yaratamiz
back = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Orqaga", callback_data='back')]
    ]
)

backk = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Orqaga", callback_data='backk')]
    ]
)