from loader import dp, db
from aiogram import types
from aiogram.dispatcher import FSMContext
from datetime import date
from keyboards.inline.admin import back


@dp.callback_query_handler(text="statistika", state='*')
async def statis(call: types.CallbackQuery, state: FSMContext):
    stat = await db.count_users()
    today = date.today()
    text = f"<b>📆 Bugunki sana: {today}\n\n📊 Bot obunachilari: {stat}\n\n⚡️@islamiuzbot</b>"
    await call.message.edit_text(text=text, reply_markup=back)
    await state.finish()