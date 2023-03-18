from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

type_sending = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👥 Guruhlarga", callback_data='intogroups'),
            InlineKeyboardButton(text="👤 Userlarga", callback_data='intousers')
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='stat_back')
        ]
    ]
)


types_group = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🖼 Surat", callback_data='withpicturegroup'),
            InlineKeyboardButton(text="📹 Video", callback_data='withvideogroup')
        ],
        [
            InlineKeyboardButton(text="📝 Text", callback_data='withtextgroup')
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='back_group')
        ]
    ]
)

types_private = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🖼 Surat", callback_data='withpictureprivate'),
            InlineKeyboardButton(text="📹 Video", callback_data='withvideoprivate')
        ],
        [
            InlineKeyboardButton(text="📝 Text", callback_data='withtextprivate')
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='to_admin_main')
        ]
    ]
)


yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Ha", callback_data='choose_ha')
        ],
        [
            InlineKeyboardButton(text="❌ Yo'q", callback_data='choose_yoq')
        ]
    ]
)

yes_no_group = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Ha", callback_data='choose_ha_group')
        ],
        [
            InlineKeyboardButton(text="❌ Yo'q", callback_data='choose_yoq_group')
        ]
    ]
)

def buttons(text, url):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.insert(
        InlineKeyboardButton(text=text, url=url)
    )
    return markup

back_group = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='back_group_adv')
        ]
    ]
)

back_privatee = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='back_private_adv')
        ]
    ]
)