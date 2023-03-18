from keyboards.inline.admin import admin
from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.prayertime import fornamoz_admin, fornamoz
from keyboards.inline.ramazon import ramazon, sanoq
from keyboards.inline.adv import types_private
from states.admin import *


# @dp.callback_query_handler(text='back', state='*')
# async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
#     await call.message.delete()
#     nphotourl = "https://t.me/forchrabot/30"
#     await call.message.answer_photo(photo=nphotourl, caption="Sizga kerakli bo'lganini tanlang👇", reply_markup=fornamoz)
#     await state.finish()

@dp.callback_query_handler(text='back', state='*')
async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    nphotourl = "https://t.me/forchrabot/30"
    await call.message.answer_photo(photo=nphotourl, caption="Sizga kerakli bo'lganini tanlang👇", reply_markup=fornamoz)
    await state.finish()

@dp.callback_query_handler(text='backk', state='*')
async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="<b>O'zingiz uchun kerakli bo'lgan bo'limni "
                                                                                "tanlang 👇🏻</b>",
                                                                        reply_markup=ramazon)
    await state.finish()

@dp.callback_query_handler(text='bacck', state='*')
async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="<b>O'zingiz uchun kerakli bo'lgan bo'limni "
                                                                                "tanlang 👇🏻</b>",
                                                                        reply_markup=ramazon)
    await state.finish()

@dp.callback_query_handler(text='tomain', state='*')
async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    nphotourl = "https://t.me/forchrabot/30"
    await call.message.answer_photo(photo=nphotourl, caption="Asosiy menuga xush kelibsiz", reply_markup=fornamoz_admin)
    await state.finish()

@dp.callback_query_handler(text='topanel', state='*')
async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Admin panel", reply_markup=admin)
    await state.finish()

@dp.callback_query_handler(text='topanell', state='*')
async def backtosubtype(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Admin panel", reply_markup=admin)
    await state.finish()


@dp.callback_query_handler(text="back_to_tabrik_ramadan", state='*')
async def back_to_ramadan(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    with open(file='media/main.png', mode='rb') as photo:
        await call.message.answer_photo(photo=photo, caption="Keraklisini tanlang👇", reply_markup=sanoq())
    await state.finish()


@dp.callback_query_handler(text="stat_back", state=Admin.stat)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await Admin.main_admin.set()



# Bu handler xabar yuborish bolimidan Admin panel menuga qaytish uchun
@dp.callback_query_handler(text="stat_back", state=Admin.sending)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await Admin.main_admin.set()




# @dp.callback_query_handler(text="stat_back", state=SendingUser.user)
# async def back_to_main(call: types.CallbackQuery, state: FSMContext):
#     user_id = call.from_user.id
#
#     text = "<b>Keraklisini tanlang👇</b>"
#     await call.message.edit_text(text=text, reply_markup=type_sending)
#     await Admin.sending.set()
#

@dp.callback_query_handler(text="bad_words_back_back", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await Admin.main_admin.set()

@dp.callback_query_handler(text="back_private_adv", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Kerakli reklama turini tanlang</b>"
    await call.message.edit_text(text=text, reply_markup=types_private)
    await SendingUser.user.set()


@dp.callback_query_handler(text="to_admin_main", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Admin panel</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await state.finish()
