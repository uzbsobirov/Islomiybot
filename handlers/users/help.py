from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message):
    text = "Agar birorta muammoga uchrasangiz yoki taklifingiz bo'lsa @menejerme"
    
    await message.answer(text=text)
