from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

typesads = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🖼 Image", callback_data='image')],
        [InlineKeyboardButton(text="📹 Video", callback_data='video')],
        [InlineKeyboardButton(text="✍️ Text", callback_data='text')],
        [InlineKeyboardButton(text="🗂 MediaGroup", callback_data="mediagroup")],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='topanell')
        ]
    ]
)