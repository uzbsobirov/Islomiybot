from loader import db, dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.prayerstate import *
import asyncio
from keyboards.inline.typeads import typesads

@dp.callback_query_handler(text="statistika", state='*')
async def statis(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    statistika = db.count_users()
    text = f"<b>📊 Botimiz a'zolari soni: {statistika[0]}\n\n🤖 @taqvimnamozbot</b>"
    await call.message.answer(text=text)
    await state.finish()

@dp.callback_query_handler(text="sendads", state='*')
async def statis(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Qaysi turdagi reklama yuborchi ekanligingizni  tanlang", reply_markup=typesads)
    await state.finish()

# Suratli reklama yuborish
@dp.callback_query_handler(text="suratli", state="*")
async def textli(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Reklama suratini yuboring📤")
    await Suratli.suratli.set()

@dp.message_handler(content_types=['photo'], state=Suratli.suratli)
async def sendadstextli(message: types.Message, state: FSMContext):
    await message.answer("Yaxshi endi reklama textini yuboring📤")
    file_id = message['photo'][0]['file_id']
    await state.update_data(
        {
            "file_id": file_id
        }
    )
    await Suratli.textli.set()

@dp.message_handler(state=Suratli.textli)
async def sendadstextli(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    file_id = data.get('file_id')
    users = db.select_all_users()
    try:
        for user in users:
            user_id = user[0]
            await bot.send_photo(chat_id=user_id, caption=text, photo=file_id)
            await asyncio.sleep(0.05)
    except Exception as error:
        print(error)
    await state.finish()



# Textli reklama yuborish
@dp.callback_query_handler(text="textli", state="*")
async def textli(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Yubormoqchi bo'lgan reklama textini yuboring📤")
    await Textli.textli.set()


@dp.message_handler(state=Textli.textli)
async def textlireklama(message: types.Message, state: FSMContext):
    text = message.text
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=text)
        await asyncio.sleep(0.05)
    await state.finish()


# Videoli reklama yuborish
@dp.callback_query_handler(text="videoli", state="*")
async def textli(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Reklama videosini yuboring📤")
    await Videoli.videoli.set()

@dp.message_handler(content_types=['video'], state=Videoli.videoli)
async def sendadstextli(message: types.Message, state: FSMContext):
    await message.answer("Yaxshi endi reklama textini yuboring📤")
    file_id = message['video']['file_id']
    await state.update_data(
        {
            "file_id": file_id
        }
    )
    await Videoli.textli.set()

@dp.message_handler(state=Videoli.textli)
async def sendadstextli(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    file_id = data.get('file_id')
    users = db.select_all_users()
    try:
        for user in users:
            user_id = user[0]
            await bot.send_video(chat_id=user_id, caption=text, video=file_id)
            await asyncio.sleep(0.05)
    except Exception as error:
        print(error)
    await state.finish()