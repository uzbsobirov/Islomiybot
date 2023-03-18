from loader import db, dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.prayerstate import *
from data.config import ADMINS
from keyboards.inline.prayertime import answer_to_admin


# Foydalanuvchi fikr bildirishi uchun
@dp.callback_query_handler(text="fikr", state='*')
async def fikrbildir(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>✍️Fikringizni yozib qoldiring!\n\n✅Adminlar uni 24 soat ichida ko'rib chiqadi!\n\n💡Iltimos " \
           "faqat text xabar yuboring</b>"
    await call.message.answer(text=text)

    await Fikr.fikr.set()


@dp.message_handler(state=Fikr.fikr)
async def fikrbildirdi(message: types.Message, state: FSMContext):
    msg = message.text
    full_name = message.from_user.full_name
    mention = message.from_user.get_mention(f"{full_name}", as_html=True)
    userid = message.from_user.id
    await state.update_data(
        {'userid': userid, 'mention': mention}
    )
    await bot.send_message(chat_id=ADMINS[0], text=f"<b>{mention} [<code>{userid}</code>]</b> botga fikr "
                                                   f"bildirdi📌\n\n <b>{msg}</b>", reply_markup=answer_to_admin)
    await message.answer(text="<b>Xabaringiz adminga jo'natildi✔️</b>")
    await state.finish()


# Fikr bildirgan foydalanuvchiga javob yozish
@dp.callback_query_handler(text="javobyozish", state='*')
async def fikrbildir(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.message.chat.id, text=f"Foydalanuvchiga yubormoqchi bo'lgan "
                                                      "xabaringizni yuboring\n\nExm: 1435473812, Your text")
    await Fikr.javob.set()


@dp.message_handler(state=Fikr.javob)
async def javob_text(message: types.Message, state: FSMContext):
    text = message.text
    user_id = text.split(',')[0]
    answer = text.split(',')[1]
    await bot.send_message(message.chat.id, text="Xabar foydalanuvchiga yuborildi")
    await bot.send_message(chat_id=user_id, text=answer)