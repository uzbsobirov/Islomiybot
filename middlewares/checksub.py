import logging
from loader import dp, db, bot
from utils.misc.subscription import check
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from data.config import CHANNELS


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ['/start', '/help']:
                return
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data in ['check_subs']:
                return
        else:
            return
        logging.info(user)
        markup = types.InlineKeyboardMarkup(row_width=1)
        final_status = True

        # rows = await db.select_row_panel()
        lst_channels = await db.select_row_panel()
        if len(lst_channels) >= 1:
            for channel in lst_channels:
                status = await check(user_id=user, channel=channel[1])
                final_status *= status
                channel = await bot.get_chat(channel[1])
                invite_link = await channel.export_invite_link()
                if not status:
                    result = "<b>Siz bizni homiy kanallardan chiqib ketgansiz❗️\n\n" \
                             "Botdan foydalanish uchun homiy kanallarimizga qayta a'zo bo'ling👇</b>"
            markup.insert(types.InlineKeyboardButton(text=channel.title, url=invite_link))
            markup.insert(types.InlineKeyboardButton(text="A'zo bo'ldim ✅", callback_data='check_subs'))

            if not final_status:
                await update.callback_query.message.delete()
                await update.callback_query.message.answer(result, reply_markup=markup, disable_web_page_preview=True)
                raise CancelHandler()

