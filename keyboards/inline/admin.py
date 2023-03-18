from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📊 Statistika", callback_data='statistika'),
            InlineKeyboardButton(text="🗞 Reklama yuborish", callback_data="sendads")
        ],
        [
            InlineKeyboardButton(text="📢 Majburiy obuna", callback_data="majburiy")
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='tomain')
        ]
    ]
)

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="◀️ Orqaga", callback_data='topanel'
            )
        ]
    ]
)