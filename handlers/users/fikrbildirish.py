from loader import db, dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.prayerstate import *
from data.config import ADMINS
from keyboards.inline.prayertime import answer_to_admin



# Foydalanuvchi fikr bildirishi uchun 
@dp.callback_query_handler(text="fikr", state='*')
async def fikrbildir(call: types.CallbackQuery, state: FSMContext):
    text = "<b>✍️Fikringizni yozib qoldiring!\n\n✅Adminlar uni 24 soat ichida ko'rib chiqadi!\n\n💡Iltimos faqat text xabar yuboring</b>"
    await call.message.answer(text=text)
    
    await Fikr.fikr.set()

@dp.message_handler(state=Fikr.fikr)
async def fikrbildirdi(message: types.Message, state: FSMContext):
    msg = message.text
    full_name = message.from_user.full_name
    user_id = message.from_user.get_mention(f"{full_name}", as_html=True)
    userid = message.from_user.id
    print(userid)
    await state.update_data({
        'userid': userid
    })
    await bot.send_message(chat_id=ADMINS[0], text=f"<b>{user_id}</b> botga fikr bildirdi📌\n\n <b>{msg}</b>", reply_markup=answer_to_admin)
    await message.answer(text="<b>Xabaringiz adminga jo'natildi✔️</b>")
    await state.finish()


# Fikr bildirgan foydalanuvchiga javob yozish
@dp.callback_query_handler(text="javobyozish", state='*')
async def fikrbildir(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data.get('user_id')