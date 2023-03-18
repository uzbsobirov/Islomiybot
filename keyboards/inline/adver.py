from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha ✅", callback_data='check_ha')
        ],
        [
            InlineKeyboardButton(text="Yo'q ❌", callback_data='check_yoq')
        ]
    ]
)


def check_ha(text, url):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton(text=text, url=url))
    return markup