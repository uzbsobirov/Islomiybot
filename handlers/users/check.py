from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp, db, bot
from utils.misc.subscription import check
from data.config import ADMINS
from keyboards.inline.prayertime import fornamoz, fornamoz_admin
@dp.callback_query_handler(text="check_subs", state='*')
async def check_func(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    full_name = call.from_user.id

    await call.answer("Obuna tekshirilmoqda...")
    final_status = True

    result = InlineKeyboardMarkup(row_width=1)

    lst_channels = await db.select_row_panel()
    # rows = await db.select_row_panel()
    if len(lst_channels) >= 1:
        for channel in lst_channels:
            status = await check(user_id=call.from_user.id, channel=channel[1])
            channel = await bot.get_chat(channel[1])
            invite_link = await channel.export_invite_link()
            if status is not True:
                final_status *= False
                result.insert(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))
        result.add(InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data='check_subs'))

        if final_status:
            await call.message.delete()
            nphotourl = "https://t.me/forchrabot/30"
            if user_id == int(ADMINS[0]):
                await call.message.answer_photo(photo=nphotourl, caption=f"<b>Assalomu aleykum {full_name}❗️\nSizni "
                                                                         "botimizda ko'rib turganimizdan xursandmiz😊\n"
                                                                         "Sizga kerakli bo'lgan bo'limni tanlang👇</b>",
                                                reply_markup=fornamoz_admin)
            else:
                await call.message.answer_photo(photo=nphotourl, caption=f"<b>Assalomu aleykum {full_name}❗️\nSizni "
                                                                "botimizda ko'rib turganimizdan xursandmiz😊\n"
                                                                "Sizga kerakli bo'lgan bo'limni tanlang👇</b>",
                                                                reply_markup=fornamoz)
            await state.finish()
        else:
            await call.message.delete()
            await call.message.answer(text="<b>❌Siz ba'zi kanallardan chiqib ketgansiz, agar kanallarga "
                                           "ulanmasangiz botni ishlata olmaysiz</b>", reply_markup=result,
                                      disable_web_page_preview=True)
            await state.finish()
    else:
        await call.message.delete()
        nphotourl = "https://t.me/forchrabot/30"
        if user_id == int(ADMINS[0]):
            await call.message.answer_photo(photo=nphotourl, caption=f"<b>Assalomu aleykum {full_name}❗️\nSizni "
                                                                     "botimizda ko'rib turganimizdan xursandmiz😊\n"
                                                                     "Sizga kerakli bo'lgan bo'limni tanlang👇</b>",
                                            reply_markup=fornamoz_admin)
        else:
            await call.message.answer_photo(photo=nphotourl, caption=f"<b>Assalomu aleykum {full_name}❗️\nSizni "
                                                                     "botimizda ko'rib turganimizdan xursandmiz😊\n"
                                                                     "Sizga kerakli bo'lgan bo'limni tanlang👇</b>",
                                            reply_markup=fornamoz)
