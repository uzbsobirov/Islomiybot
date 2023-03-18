from loader import dp
from keyboards.inline.ramazon import ramazon
from states.ramazon import Ramadan
from keyboards.inline.back import backk
from keyboards.inline.ramazon import sanoq, share
from states.card import Type


from aiogram import types
from aiogram.dispatcher import FSMContext
from PIL import Image, ImageDraw, ImageFont

# Main menu
@dp.callback_query_handler(text="ramazonbolimi", state='*')
async def ramazon_bolimi(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>O'zingiz uchun kerakli bo'lgan bo'limni tanlang 👇🏻</b>"
    await call.message.answer(text=text, reply_markup=ramazon)


# Ogiz ochish
@dp.callback_query_handler(text='ogizochish', state='*')
async def ogiz_ochish(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    caption = "<b>Ифторлик (оғиз очиш) дуоси ✨\n\nАллоҳумма лака сумту ва бика ааманту ва аълайка " \
              "таваккалту ва аълаа ризқика афтарту, фағфирлий ма қоддамту ва маа аххорту бироҳматика " \
              "йаа арҳамар рооҳимийн.\n\nМаъноси: Эй Аллоҳ, ушбу Рўзамни Сен учун тутдим ва Сенга иймон " \
              "келтирдим ва Сенга таваккал қилдим ва берган ризқинг билан ифтор қилдим. Эй меҳрибонларнинг " \
              "энг меҳрибони, менинг аввалги ва кейинги гуноҳларимни мағфират қилгил.</b>"
    # We get photo
    with open(file='media/ogizochish.png', mode='rb') as photo:
        await call.message.answer_photo(photo=photo, caption=caption, reply_markup=backk)
    await state.finish()


# Ogiz yopish
@dp.callback_query_handler(text='ogizyopish', state='*')
async def ogiz_ochish(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    caption = "<b>Рўза тутиш (саҳарлик, оғиз ёпиш) дуоси ✨\n\n" \
              "Навайту ан асувма совма шаҳри рамазона минал фажри илал мағриби, " \
              "холисан лиллаҳи таъаалаа Аллоҳу акбар.\n\nМаъноси: Рамазон ойининг " \
              "рўзасини субҳдан то кун ботгунча тутмоқни ният қилдим. Холис Аллоҳ учун Аллоҳ буюкдир.</b>"
    # We get photo
    with open(file='media/ogizyopish.png', mode='rb') as photo:
        await call.message.answer_photo(photo=photo, caption=caption, reply_markup=backk)
    await state.finish()


# Tabrik
@dp.callback_query_handler(text="ramazontabrik", state='*')
async def ramazon_tabrik(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    with open(file='media/main.png', mode='rb') as photo:
        await call.message.answer_photo(photo=photo, caption="Keraklisini tanlang👇", reply_markup=sanoq())
    await state.finish()

@dp.callback_query_handler(text="type-1")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type1.set()

@dp.message_handler(state=Type.type1)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/type-1.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 36)
    text_size = draw.textbbox((100, 100), text, font=font)

    x = ((img.width - text_size[2]) / 2) + 50
    y = 210

    draw.text((x, y), text, font=font, fill='white')
    img.save("media/results.png")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
              "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/islamiuzbot"
    with open(file='media/results.png', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="type-2")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type2.set()

@dp.message_handler(state=Type.type2)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/type-2.png")
    draw = ImageDraw.Draw(img)
    if len(text) <= 5:
        font = ImageFont.truetype("media/cabal.ttf", 36)
        x = 42
        y = 225

        draw.text((x, y), text, font=font, fill='white')
    else:
        font = ImageFont.truetype("media/cabal.ttf", 24)
        x = 40
        y = 240

        draw.text((x, y), text, font=font, fill='white')
    text_size = draw.textbbox((100, 100), text, font=font)

    img.save("media/results.png")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
              "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/islamiuzbot"
    with open(file='media/results.png', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="type-3")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type3.set()

@dp.message_handler(state=Type.type3)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/type-3.png")
    draw = ImageDraw.Draw(img)
    if len(text) <= 5:
        font = ImageFont.truetype("media/cabal.ttf", 36)
        x = 42
        y = 225

        draw.text((x, y), text, font=font, fill='white')
    else:
        font = ImageFont.truetype("media/cabal.ttf", 24)
        x = 40
        y = 240

        draw.text((x, y), text, font=font, fill='white')
    text_size = draw.textbbox((100, 100), text, font=font)

    img.save("media/results.png")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
              "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/islamiuzbot"
    with open(file='media/results.png', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="type-4")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type4.set()

@dp.message_handler(state=Type.type4)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/type-4.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 36)
    text_size = draw.textbbox((100, 100), text, font=font)

    x = ((img.width - text_size[2]) / 2) + 50
    y = 340

    draw.text((x, y), text, font=font, fill='white')

    text_size = draw.textbbox((100, 100), text, font=font)

    img.save("media/results.png")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
              "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/islamiuzbot"
    with open(file='media/results.png', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="type-5")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type5.set()

@dp.message_handler(state=Type.type5)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/type-5.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 36)
    text_size = draw.textbbox((100, 100), text, font=font)

    x = ((img.width - text_size[2]) / 2) + 50
    y = 240

    draw.text((x, y), text, font=font, fill='white')

    text_size = draw.textbbox((100, 100), text, font=font)

    img.save("media/results.png")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
              "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/islamiyuzbot"
    with open(file='media/results.png', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="type-6")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type6.set()

@dp.message_handler(state=Type.type6)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/type-6.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 36)
    text_size = draw.textbbox((100, 100), text, font=font)

    x = ((img.width - text_size[2]) / 2) + 50
    y = 180

    draw.text((x, y), text, font=font, fill='black')

    text_size = draw.textbbox((100, 100), text, font=font)

    img.save("media/results.png")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
              "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/islamiuzbot"
    with open(file='media/results.png', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="type-7")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type7.set()

@dp.message_handler(state=Type.type7)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/type-7.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 36)
    text_size = draw.textbbox((100, 100), text, font=font)

    x = ((img.width - text_size[2]) / 2) + 50
    y = 200

    draw.text((x, y), text, font=font, fill='white')

    text_size = draw.textbbox((100, 100), text, font=font)

    img.save("media/results.png")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
              "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/islamiuzbot"
    with open(file='media/results.png', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="type-8")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type8.set()

@dp.message_handler(state=Type.type8)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/type-8.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 36)
    text_size = draw.textbbox((100, 100), text, font=font)

    x = ((img.width - text_size[2]) / 2) + 50
    y = 200

    draw.text((x, y), text, font=font, fill='white')

    text_size = draw.textbbox((100, 100), text, font=font)

    img.save("media/results.png")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
              "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/islamiuzbot"
    with open(file='media/results.png', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()

@dp.callback_query_handler(text="type-9")
async def number_func(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    text = "<b>Kim uchun tayyorlaymiz?</b>\n<i>Ism yozib yuboring...</i>"
    await call.message.answer(text=text)
    await Type.type9.set()

@dp.message_handler(state=Type.type9)
async def satte_type1(message: types.Message, state: FSMContext):
    text = message.text

    img = Image.open("media/type-9.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("media/cabal.ttf", 36)
    text_size = draw.textbbox((100, 100), text, font=font)

    x = ((img.width - text_size[2]) / 2) + 50
    y = 265

    draw.text((x, y), text, font=font, fill='#154c79')

    text_size = draw.textbbox((100, 100), text, font=font)

    img.save("media/results.png")
    url = "http://telegram.me/share/url?url=%20Do'stlar%20Bu%20Bot%20judaham%20zo'r" \
              "%20ekan%20siz%20ham%20harxil turdagi%20Tabriklar%20yasab%20oling%20%20http://t.me/islamiuzbot"
    with open(file='media/results.png', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=f'{text} ismiga rasm tayyor✅', reply_markup=share(url=url))
        await state.finish()