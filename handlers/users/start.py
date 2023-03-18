from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext

from keyboards.inline.prayertime import fornamoz, fornamoz_admin
from data.config import ADMINS
from loader import dp, db, bot
from utils.misc.subscription import check
from data.config import CHANNELS


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    mention = message.from_user.get_mention(name=full_name)

    # Foydalanuvchini bazaga qo'shamiz
    try:
        await db.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id
        )

        # Adminga xabar beramiz
        msg = f"{mention} bazaga qo'shildi.\n"
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except:
        await bot.send_message(chat_id=ADMINS[0], text=f"{mention} bazaga oldin qo'shilgan")

    # User malumotlarini olamiz
    lst_channels = await db.select_row_panel()
    if len(lst_channels) >= 1:
        # We check if user is not subs to channel
        for row in lst_channels:
            status = await check(user_id=message.from_user.id, channel=row[1])
        if status == False:
            markup = InlineKeyboardMarkup(row_width=1)
            for channel in lst_channels:
                chat = await bot.get_chat(channel[1])
                invite_link = await chat.export_invite_link()
                markup.insert(InlineKeyboardButton(text=chat.title, url=invite_link))
            markup.add(InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data='check_subs'))

            text = f"<b>Assalomu aleykum</b>, {full_name}! Botdan to'liq foydalanish uchun homiy kanallarimizga a'zo " \
                   f"bo'ling"
            await message.answer(text=text, reply_markup=markup, disable_web_page_preview=True)
            await state.finish()
        else:
            nphotourl = "https://t.me/forchrabot/30"
            if user_id == int(ADMINS[0]):
                await message.answer_photo(photo=nphotourl, caption=f"<b>Sizga kerakli bo'lgan bo'limni tanlang👇</b>",
                                           reply_markup=fornamoz_admin)
            else:
                await message.answer_photo(photo=nphotourl, caption=f"<b>Sizga kerakli bo'lgan bo'limni tanlang👇</b>",
                                            reply_markup=fornamoz)
    else:
        nphotourl = "https://t.me/forchrabot/30"
        if user_id == int(ADMINS[0]):
            await message.answer_photo(photo=nphotourl, caption=f"<b>Assalomu aleykum {full_name}❗️\nSizni "
                                                                "botimizda ko'rib turganimizdan xursandmiz😊\n"
                                                                "Sizga kerakli bo'lgan bo'limni tanlang👇</b>",
                                       reply_markup=fornamoz_admin)
        else:
            await message.answer_photo(photo=nphotourl, caption=f"<b>Assalomu aleykum {full_name}❗️\nSizni "
                                                            "botimizda ko'rib turganimizdan xursandmiz😊\n"
                                                            "Sizga kerakli bo'lgan bo'limni tanlang👇</b>",
                                   reply_markup=fornamoz)