import json
import codecs
from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.prayerstate import Quran
from keyboards.inline.back import back

# Quronni o'qib olish uchun
with codecs.open('verses.json', 'r', encoding='utf-8', errors='ignore') as file:
    verses = json.load(file)
    quran = verses['quran']


# Quranni chiqarish uchun
@dp.callback_query_handler(text="qurans", state='*')
async def qurans(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Sizga nechanchi bob kerak? Sonlarda kiriting👇👇👇</b>")
    await Quran.chapter.set()


@dp.message_handler(state=Quran.chapter)
async def quran_bob(message: types.Message, state: FSMContext):
    chapter = message.text
    await message.answer(f"<b>{chapter}-bobning nechanchi oyati kerak?👇👇👇</b>")
    await state.update_data(
        {'chapter': int(chapter)}
    )
    await Quran.verse.set()


@dp.message_handler(state=Quran.verse)
async def quran_bob(message: types.Message, state: FSMContext):
    data = await state.get_data()
    chapter = data.get('chapter')
    verse = int(message.text)
    for what in quran:
        if chapter == what['chapter']:
            if verse == what['verse']:
                await message.answer(text=what['text'], reply_markup=back)
                await state.finish()
                break



