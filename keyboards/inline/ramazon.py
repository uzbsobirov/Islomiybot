from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ramazon = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Ramazon tabriklar ✨", callback_data='ramazontabrik'
            )
        ],
        [
            InlineKeyboardButton(
                text="Og'iz ochish duosi 🤲", callback_data='ogizochish'
            ),
            InlineKeyboardButton(
                text="Og'iz yopish duosi 🤲🏻", callback_data='ogizyopish'
            )
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='back')
        ]
    ]
)

def sanoq():
    markup = InlineKeyboardMarkup(row_width=3)
    for i in range(1, 10):
        markup.insert(
            InlineKeyboardButton(
                text=f"{i}", callback_data=f'type-{i}'
            )
        )
    markup.add(
        InlineKeyboardButton(text="◀️ Orqaga", callback_data='bacck')
    )
    return markup


def share(url):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.insert(
        InlineKeyboardButton(
            text="⤴️ Do'stlarga ulashish",
            url=url
        )
    )
    markup.insert(
        InlineKeyboardButton(
            text="◀️ Orqaga", callback_data='back_to_tabrik_ramadan'
        )
    )
    return markup