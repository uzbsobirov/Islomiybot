import asyncio
from loader import db, dp, bot
from states.adv import *
from keyboards.inline.adv import yes_no, buttons, back_privatee, types_private

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text="sendads", state='*')
async def type_of_adv(call: types.CallbackQuery, state: FSMContext):
    text = "<b>O'zingizga kerakli reklama turini tanlang</b>"
    await call.message.edit_text(text=text, reply_markup=types_private)


# <------------Adver with photo and text------------->
@dp.callback_query_handler(text="withpictureprivate", state='*')
async def odinochit(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Reklama rasmini yuboring, faqat rasmni!")
    await Picture.file_id.set()

@dp.message_handler(state=Picture.file_id, content_types=types.ContentType.PHOTO)
async def file_id_image(message: types.Message, state: FSMContext):
    image_file_id = message.photo[-1].file_id
    await state.update_data(
        {'image_file_id': image_file_id}
    )

    await message.answer(text="Yaxshi endi reklama textini yuboring")
    await Picture.text.set()

@dp.message_handler(state=Picture.text)
async def image_tekst(message: types.Message, state: FSMContext):
    image_text = message.text
    await state.update_data(
        {'image_text': image_text}
    )

    await message.answer(text="Tugma qo'shishni xoxlaysizmi?", reply_markup=yes_no)
    await Picture.choose_yes_no.set()

@dp.callback_query_handler(state=Picture.choose_yes_no)
async def choose_yes_no_data(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    image_file_id = data.get('image_file_id')
    image_text = data.get('image_text')


    await call.message.delete()
    if call.data == 'choose_yoq':
        await state.finish()

        success_send = 0
        not_send = 0
        users = await db.select_all_users()
        for user in users:
            user_id = user[3]
            try:
                await bot.send_photo(chat_id=user_id, photo=image_file_id, caption=image_text)
                await asyncio.sleep(1)
                success_send += 1
            except Exception as error:
                print(error)
                not_send += 1
                continue

        await call.message.answer(text=f"<b>✅ Reklama <i>{success_send}</i> ta foydalanuvchiga muvaffaqqiyatli "
                                                       f"yuborildi\n\n"
                                                  f"❌ Reklama <i>{not_send}</i> ta foydalanuvchiga bormadi</b>"
                                  , reply_markup=back_privatee)

    else:
        choose_text = "<b>Tugma qo'shmoqchi bo'lsangiz namunadagidek qilib yuboring👇\n\n" \
                      "<code>Foydali botlar+https://t.me/kayzenuz</code></b>"
        await call.message.answer(text=choose_text)
        await Picture.choose_yes.set()

@dp.message_handler(state=Picture.choose_yes)
async def user_choose_ha_image(message: types.Message, state: FSMContext):
    btn_link = message.text
    split_text = btn_link.split('+')
    adv_text = split_text[0]
    adv_url = split_text[1]

    data = await state.get_data()
    image_file_id = data.get('image_file_id')
    image_text = data.get('image_text')

    success_send = 0
    not_send = 0
    users = await db.select_all_users()
    for user in users:
        user_id = user[3]
        try:
            await bot.send_photo(chat_id=user_id, photo=image_file_id, caption=image_text,
                                                    reply_markup=buttons(text=adv_text, url=adv_url))
            await asyncio.sleep(1)
            success_send += 1
        except Exception as error:
            print(error)
            not_send += 1
            continue
        await state.finish()

    await message.answer(
        text=f"<b>✅ Reklama <i>{success_send}</i> ta foydalanuvchiga muvaffaqqiyatli yuborildi\n\n"
             f"❌ Reklama <i>{not_send}</i> ta foydalanuvchiga bormadi</b>", reply_markup=back_privatee)


# <------------Adver with text------------->
@dp.callback_query_handler(text="withtextprivate", state='*')
async def withtextprivate(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Reklama textini yuboring")
    await Text.text.set()

@dp.message_handler(state=Text.text)
async def text_texti(message: types.Message, state: FSMContext):
    text_text = message.text

    await state.update_data(
        {'text_text': text_text}
    )
    await message.answer(text="Tugma qo'shishni xoxlaysizmi?", reply_markup=yes_no)
    await Text.choose_yes_no.set()

@dp.callback_query_handler(state=Text.choose_yes_no)
async def choose_yes_no(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('text_text')

    await call.message.delete()

    if call.data == 'choose_yoq':
        await state.finish()

        success_send = 0
        not_send = 0

        users = await db.select_all_users()
        for user in users:
            user_id = user[3]
            try:
                await bot.send_message(chat_id=user_id, text=text)
                await asyncio.sleep(1)
                success_send += 1
            except Exception as error:
                print(error)
                not_send += 1
                continue
        await call.message.answer(
            text=f"<b>✅ Reklama <i>{success_send}</i> ta foydalanuvchiga muvaffaqqiyatli yuborildi\n\n"
                 f"❌ Reklama <i>{not_send}</i> ta foydalanuvchiga bormadi</b>", reply_markup=back_privatee)

    else:
        choose_text = "<b>Tugma qo'shmoqchi bo'lsangiz namunadagidek qilib yuboring👇\n\n" \
                      "<code>Foydali botlar+https://t.me/kayzenuz</code></b>"
        await call.message.answer(text=choose_text)
        await Text.choose_yes.set()

@dp.message_handler(state=Text.choose_yes)
async def user_choose_ha_image(message: types.Message, state: FSMContext):
    btn_link = message.text
    split_text = btn_link.split('+')
    adv_text = split_text[0]
    adv_url = split_text[1]

    data = await state.get_data()
    text = data.get('text_text')

    not_send = 0
    success_send = 0
    users = await db.select_all_users()
    for user in users:
        user_id = user[3]
        try:
            await bot.send_message(chat_id=user_id, text=text,
                                                    reply_markup=buttons(text=adv_text, url=adv_url))
            await asyncio.sleep(1)
            success_send += 1
        except Exception as error:
            print(error)
            not_send += 1
            continue

        await state.finish()
    await message.answer(text=f"<b>✅ Reklama <i>{success_send}</i> ta foydalanuvchiga muvaffaqqiyatli yuborildi\n\n"
                                        f"❌ Reklama <i>{not_send}</i> ta foydalanuvchiga bormadi</b>", reply_markup=back_privatee)

# <------------Adver with video and text------------->
@dp.callback_query_handler(text="withvideoprivate", state='*')
async def odinochit(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Reklama videosini yuboring, faqat videoni!")
    await Video.file_id.set()

@dp.message_handler(state=Video.file_id, content_types=types.ContentType.VIDEO)
async def file_id_image(message: types.Message, state: FSMContext):
    video_file_id = message.video.file_id
    await state.update_data(
        {'video_file_id': video_file_id}
    )

    await message.answer(text="Yaxshi endi reklama textini yuboring")
    await Video.text.set()

@dp.message_handler(state=Video.text)
async def image_tekst(message: types.Message, state: FSMContext):
    video_text = message.text
    await state.update_data(
        {'video_text': video_text}
    )

    await message.answer(text="Tugma qo'shishni xoxlaysizmi?", reply_markup=yes_no)
    await Video.choose_yes_no.set()

@dp.callback_query_handler(state=Video.choose_yes_no)
async def choose_yes_no_data(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    video_file_id = data.get('video_file_id')
    video_text = data.get('video_text')


    await call.message.delete()
    if call.data == 'choose_yoq':
        await state.finish()
        not_send = 0
        success_send = 0

        users = await db.select_all_users()
        for user in users:
            user_id = user[3]
            try:
                await bot.send_video(chat_id=user_id, video=video_file_id, caption=video_text)
                await asyncio.sleep(1)
                success_send += 1
            except Exception as error:
                print(error)
                not_send += 1
                continue
        await call.message.answer(
            text=f"<b>✅ Reklama <i>{success_send}</i> ta foydalanuvchiga muvaffaqqiyatli yuborildi\n\n"
                 f"❌ Reklama <i>{not_send}</i> ta foydalanuvchiga bormadi</b>", reply_markup=back_privatee)

    else:
        choose_text = "<b>Tugma qo'shmoqchi bo'lsangiz namunadagidek qilib yuboring👇\n\n" \
                      "<code>Foydali botlar+https://t.me/kayzenuz</code></b>"
        await call.message.answer(text=choose_text)
        await Video.choose_yes.set()

@dp.message_handler(state=Video.choose_yes)
async def user_choose_ha_image(message: types.Message, state: FSMContext):
    btn_link = message.text
    split_text = btn_link.split('+')
    adv_text = split_text[0]
    adv_url = split_text[1]

    data = await state.get_data()
    video_file_id = data.get('video_file_id')
    video_text = data.get('video_text')

    not_send = 0
    success_send = 0
    users = await db.select_all_users()
    for user in users:
        user_id = user[3]
        try:
            await bot.send_video(chat_id=user_id, video=video_file_id, caption=video_text,
                                                    reply_markup=buttons(text=adv_text, url=adv_url))
            await asyncio.sleep(1)
            success_send += 1
        except Exception as error:
            print(error)
            not_send += 1
            continue
        await state.finish()

    await message.answer(
        text=f"<b>✅ Reklama <i>{success_send}</i> ta foydalanuvchiga muvaffaqqiyatli yuborildi\n\n"
             f"❌ Reklama <i>{not_send}</i> ta foydalanuvchiga bormadi</b>", reply_markup=back_privatee)