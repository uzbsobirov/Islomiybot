from loader import dp
from aiogram import types
from states.prayerstate import Prayer
from aiogram.dispatcher import FSMContext
from keyboards.inline.prayertime import fornamoz

@dp.callback_query_handler(text='back', state='*')
async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    nphotourl = "https://t.me/forchrabot/30"
    await call.message.answer_photo(photo=nphotourl, caption="Sizga kerakli bo'lganini tanlang👇", reply_markup=fornamoz)
    await state.finish()
