from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

add_sponsor = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ Kanal qo'shish", callback_data='addsponsor')
        ],
        [
            InlineKeyboardButton(text="🗑 Kanalni o'chirish", callback_data='deletesponsor')
        ]
    ]
)

sponsor_add = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ Yana qo'shish", callback_data='addsponsor')
        ]
    ]
)