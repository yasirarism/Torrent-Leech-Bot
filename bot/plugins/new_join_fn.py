#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | @Technical-Jigar

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram


from bot import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    #channel_id = str(AUTH_CHANNEL)[4:]
    #message_id = 99
    # display the /help
    
    await message.reply_text("""/leech - upload Magnet/direct link to telegram file: reply to a link.

/leech archive: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [This command will create a .tar.gz file of the output directory, and send the files in the chat, splited into PARTS of 1024MiB each, due to Telegram limitations]

/leech unzip: This will unzip the .zip file and dupload to telegram.

/leech unrar: This will unrar the .rar file and dupload to telegram.

/leech untar: This will unrar the .tar file and dupload to telegram.

/ytdl - upload from any Youtube-dl supportd url to telegram file: reply to a link.

/pytdl -upload from any Youtube-dl supportd playlist to telegram files: reply to a link.

/savethumbnail - set custom thumbnail: send a pic first than replay on that pic.

/clearthumbnail - clear default thumbnail.

/status - Show all download status.

/cancel - cancel upload:reply to your sent link.

/log - get log file.

/help - to see this msg.
⚡ @Universal_Fast_Mirror ⚡""", disable_web_page_preview=True, parse_mode="markdown")


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="read this?",
            url="https://t.me/keralagram/698909"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "please use @renamebot",
        quote=True,
        reply_markup=reply_markup
    )
