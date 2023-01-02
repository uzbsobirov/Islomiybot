from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

fornamoz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👳Erkaklar Uchun", callback_data="namozboy"),
            InlineKeyboardButton(text="🧕Ayollar Uchun", callback_data="namozgirl"),
        ],
        [
            InlineKeyboardButton(text="🕔 Namoz vaqtlari", callback_data='namoztime')
        ],
    ]
)



fornamoztimeboy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bomdod", callback_data="bomdodboy"),
            InlineKeyboardButton(text="Peshin", callback_data="peshinboy")
        ],
        [
            InlineKeyboardButton(text="Asr", callback_data='asrboy'),
            InlineKeyboardButton(text="Shom", callback_data='shomboy')
        ],
        [
            InlineKeyboardButton(text="Xufton", callback_data='xuftonboy'),
            InlineKeyboardButton(text="Duolar", callback_data='duoboy')
        ],
        [
            InlineKeyboardButton(text="Janoza Namozi", callback_data='janozaboy'),
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='back')
        ]
    ]
)

##Girl
fornamoztimegirl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bomdod", callback_data="bomdodgirl"),
            InlineKeyboardButton(text="Peshin", callback_data="peshingirl")
        ],
        [
            InlineKeyboardButton(text="Asr", callback_data='asrgirl'),
            InlineKeyboardButton(text="Shom", callback_data='shomgirl')
        ],
        [
            InlineKeyboardButton(text="Xufton", callback_data='xuftongirl'),
            InlineKeyboardButton(text="Duolar", callback_data='duogirl')
        ],
        [
            InlineKeyboardButton(text="Janoza Namozi", callback_data='janozagril'),
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='back')
        ]
    ]
)