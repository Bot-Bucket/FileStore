#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ᴍɪᴋᴇʏ</a>\n○ ᴇᴀʀɴɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Earning_Bucket'>ᴇᴀʀɴɪɴɢ ʙᴜᴄᴋᴇᴛ</a>\n○ ʙᴏᴛs ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Bucket_Bots'>ʙᴜᴄᴋᴇᴛ ʙᴏᴛᴢ</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/BDNetwork'>ʙᴅɴᴇᴛᴡᴏʀᴋ</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ ɢʀᴏᴜᴘ : <a href='https://t.me/Anime_in_Hindi_Chat_Group'>ᴀɴɪᴍᴇ ɪɴ ʜɪɴᴅɪ ᴄʜᴀᴛ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/+ZD2Mnl_dL8piNWNl')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
