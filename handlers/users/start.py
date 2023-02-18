import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.prayertime import fornamoz
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        nphotourl = "https://t.me/forchrabot/30"
        await message.answer_photo(photo=nphotourl, caption=f"<b>Assalomu aleykum {name}❗️\n"
                                                            "Sizni botimizda ko'rib turganimizdan xursandmiz😊\n"
                                                            "Sizga kerakli bo'lgan bo'limni tanlang👇</b>",
                                                            reply_markup=fornamoz)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        nphotourl = "https://t.me/forchrabot/30"
        await message.answer_photo(photo=nphotourl, caption=f"<b>Assalomu aleykum {name}❗️\nSizni "
                                                            "botimizda ko'rib turganimizdan xursandmiz😊\n"
                                                            "Sizga kerakli bo'lgan bo'limni tanlang👇</b>",
                                                            reply_markup=fornamoz)
