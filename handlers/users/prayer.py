from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.prayerstate import Prayer
import requests
# from keyboards.default.main_menu import mainboard
from keyboards.inline.back import back
from keyboards.inline.prayertime import (fornamoz, fornamoztimeboy,
                                         fornamoztimegirl)
# from keyboards.inline.btn_back import turnback

# from states.default_btn import MyState

# from keyboards.default.fordownload import downbtn





@dp.callback_query_handler(text="namoztime", state='*')
async def namoztime(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Viloyatingiz yoki tumaningiz nomini kiritng👇\n(Hech qanday imlo hatolarsiz❗️)")
    await Prayer.timetype.set()

@dp.message_handler(state=Prayer.timetype)
async def namozvaqti(message: types.Message, state: FSMContext):
    msg = message.text
    try:
        req = f"https://islomapi.uz/api/present/day?region={msg}"
        response = requests.get(url=req).json()
        text = f"\n\n<b><i>📆 Bugunki sana</i></b>: <b>{response['date']}</b>\n<b><i>〽️ Bugunki kun</i></b>: <b>{response['weekday']}</b>\n<i><b>🏢 Shaxar</b></i> - <b>( {response['region']} )</b>\n\n<b><i>🌇 Tong saharlik</i></b> - <b>{response['times']['tong_saharlik']}</b>\n\n<b><i>🌅 Quyosh</i></b> - <b>{response['times']['quyosh']}</b>\n\n<b><i>🏞 Peshin</i></b> - <b>{response['times']['peshin']}</b>\n\n<b><i>🌇 Asr</i></b> - <b>{response['times']['asr']}</b>\n\n<b><i>🌄 Shom</i></b> - <b>{response['times']['shom_iftor']}</b>\n\n<b><i>🌃 Hufton</i></b> - <b>{response['times']['hufton']}</b>\n\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n\nوَٱللَّهُ يُرِيدُ أَن يَتُوبَ عَلَيۡكُمۡ وَيُرِيدُ ٱلَّذِينَ يَتَّبِعُونَ ٱلشَّهَوَٰتِ أَن تَمِيلُواْ مَيۡلًا عَظِيمٗا\n\nАlloh sizning tavbangizni qabul qilishni xohlaydir. Shahvatlarga ergashadiganlar esa, ulkan ogʼishga moyil boʼlishingizni xohlaydir.\n\n▫️Niso Surasi 27-oyat\n\n"
        await message.answer(text=text, reply_markup=back)
        await state.finish()
    except:
        await message.answer("Bunday shahar yoki tuman yo'q")
        await Prayer.timetype.set()

    






@dp.callback_query_handler(text="namozboy", state='*')
async def namozboy(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("O'zingizga kerakli vaqtni tanlang👇", reply_markup=fornamoztimeboy)
    await Prayer.videotype.set()

@dp.callback_query_handler(text="bomdodboy", state=Prayer.videotype)
async def bomdodboy(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    
    bomdodurl = "https://t.me/forchrabot/31"
    await call.message.answer_video(video=bomdodurl, caption="Erkaklar uchun <b>Bomdod</b> namozining to'liq o'qilish tartibi", reply_markup=back, parse_mode='html')
    await state.finish()


@dp.callback_query_handler(text="peshinboy", state=Prayer.videotype)
async def peshinboy(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    peshinurl = "https://t.me/forchrabot/32"
    await call.message.answer_video(video=peshinurl, caption="Erkaklar uchun <b>Peshin</b> namozining to'liq o'qilish tartibi", reply_markup=back, parse_mode='html')
    await state.finish()



@dp.callback_query_handler(text="asrboy", state=Prayer.videotype)
async def asrboy(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    asrurl = "https://t.me/forchrabot/33"
    await call.message.answer_video(video=asrurl, caption="Erkaklar uchun <b>Asr</b> namozining to'liq o'qilish tartibi", reply_markup=back, parse_mode='html')
    await state.finish()



@dp.callback_query_handler(text="shomboy", state=Prayer.videotype)
async def shomboy(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    shomurl = "https://t.me/forchrabot/34"
    await call.message.answer_video(video=shomurl, caption="Erkaklar uchun <b>Shom</b> namozining to'liq o'qilish tartibi", reply_markup=back, parse_mode='html')
    await state.finish()


@dp.callback_query_handler(text="janozaboy", state=Prayer.videotype)
async def janozaboy(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    janozaboy = "https://t.me/forchrabot/43"
    await call.message.answer_video(video=janozaboy, caption="Erkaklar uchun <b>Janoza</b> namozining to'liq o'qilish tartibi", reply_markup=back, parse_mode='html')
    await state.finish()



@dp.callback_query_handler(text="xuftonboy", state=Prayer.videotype)
async def xuftonboy(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    xuftonurl = "https://t.me/forchrabot/35"
    await call.message.answer_video(video=xuftonurl, caption="Erkaklar uchun <b>Xufton</b> namozining to'liq o'qilish tartibi", reply_markup=back, parse_mode='html')
    await state.finish()



@dp.callback_query_handler(text="duoboy", state=Prayer.videotype)
async def duoboy(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    msg = """NAMOZDAN KEYINGI ZIKRLAR

Namoz salom bilan tugaydi. Salomdan keyingi amallar (tasbehotu duolar) majburiy emas, ammo nihoyatda savoblidir.
Farz namozlaridan keyin quyidagi duoni o‘qish sunnatdir:
Allohumma antas-salam va minkas-salam. Tabarokta ya zaljalali val ikrom.
Mazmuni:
Ey Allohim, Sen barcha ayb-nuqsonlardan poksan. Barcha salomatlik va rahmat Sendandir. Ey azamat va qudrat egasi bo‘lgan Allohim, Sening shoning ulug‘dir.
Umuman, har vaqt namozni tugatgandan so‘ng Oyatal kursi o‘qilsa, tasbehot qilinsa, savobi ulug‘ bo‘ladi."""
    await call.message.answer(text=msg, reply_markup=back)
    await state.finish()



#<<Ayollar<<
@dp.callback_query_handler(text="namozgirl",state='*')
async def namozgirl(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    # namozgirl = "https://t.me/forchrabot/37"
    await call.message.answer("O'zingizga kerakli vaqtni tanlang👇", reply_markup=fornamoztimegirl)
    await Prayer.videotype.set()

@dp.callback_query_handler(text="bomdodgirl", state=Prayer.videotype)
async def bomdodgirl(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    bomdodgirl = "https://t.me/forchrabot/37"
    await call.message.answer_video(video=bomdodgirl, caption="Ayollar uchun <b>Bomdod</b> namozining to'liq o'qilish tartibi", parse_mode='html', reply_markup=back)
    await state.finish()


@dp.callback_query_handler(text="peshingirl", state=Prayer.videotype)
async def peshingirl(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    peshingirl = "https://t.me/forchrabot/38"
    await call.message.answer_video(video=peshingirl, caption="Ayollar uchun <b>Peshin</b> namozining o'qilish tartibi", parse_mode='html', reply_markup=back)
    await state.finish()



@dp.callback_query_handler(text="asrgirl", state=Prayer.videotype)
async def asrgirl(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    asrgirl = "https://t.me/forchrabot/39"
    await call.message.answer_video(video=asrgirl, caption="Ayollar uchun <b>Asr</b> namozining o'qilish tartibi", parse_mode='html', reply_markup=back)
    await state.finish()

@dp.callback_query_handler(text="shomgirl", state=Prayer.videotype)
async def shomgirl(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    shomgirl = "https://t.me/forchrabot/40"
    await call.message.answer_video(video=shomgirl, caption="Ayollar uchun <b>Shom</b> namozining o'qilish tartibi", parse_mode='html', reply_markup=back)
    await state.finish()


@dp.callback_query_handler(text="xuftongirl", state=Prayer.videotype)
async def xuftongirl(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.finish()
    xuftongirl = "https://t.me/forchrabot/41"
    await call.message.answer_video(video=xuftongirl, caption="Ayollar uchun <b>Xufton</b> namozining o'qilish tartibi", parse_mode='html', reply_markup=back)
    await state.finish()
    



@dp.callback_query_handler(text="duogirl", state=Prayer.videotype)
async def duogirl(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    msg = """NAMOZDAN KEYINGI ZIKRLAR

Namoz salom bilan tugaydi. Salomdan keyingi amallar (tasbehotu duolar) majburiy emas, ammo nihoyatda savoblidir.
Farz namozlaridan keyin quyidagi duoni o‘qish sunnatdir:
Allohumma antas-salam va minkas-salam. Tabarokta ya zaljalali val ikrom.
Mazmuni:
Ey Allohim, Sen barcha ayb-nuqsonlardan poksan. Barcha salomatlik va rahmat Sendandir. Ey azamat va qudrat egasi bo‘lgan Allohim, Sening shoning ulug‘dir.
Umuman, har vaqt namozni tugatgandan so‘ng Oyatal kursi o‘qilsa, tasbehot qilinsa, savobi ulug‘ bo‘ladi."""
    await call.message.answer(text=msg, reply_markup=back)
    await state.finish()









# @dp.callback_query_handler(text="back", state=MyState.namozmahal)
# async def back(call: types.CallbackQuery, state: FSMContext):
#     await call.message.delete()
    
#     nphotourl = "https://t.me/forchrabot/30"
#     await call.message.answer_photo(photo=nphotourl, caption="Sizga kerakli bo'lganini tanlang👇", reply_markup=fornamoz)
#     await MyState.prayertime.set()