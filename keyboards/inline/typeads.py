from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

typesads = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🖼 Suratli", callback_data='suratli')],
        [InlineKeyboardButton(text="📹 Videoli", callback_data='videoli')],
        [InlineKeyboardButton(text="✍️ Textli", callback_data='textli')],
        [InlineKeyboardButton(text="🗂 MediaGroup", callback_data="mediagroup")]
    ]
)