#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52 | @Technical-Jigar

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os
import io
import sys
import traceback

from bot import (
    DOWNLOAD_LOCATION,
    TG_BOT_TOKEN,
    APP_ID,
    API_HASH,
    AUTH_CHANNEL,
    LEECH_COMMAND,
    YTDL_COMMAND,
    CANCEL_COMMAND_J,
    STATUS_COMMAND,
    SAVE_THUMBNAIL,
    CLEAR_THUMBNAIL,
    PYTDL_COMMAND_J,
    LOG_COMMAND,
    BOT_USERNAME,
)

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler

from bot.plugins.new_join_fn import new_join_f, help_message_f, rename_message_f
from bot.plugins.incoming_message_fn import incoming_message_f, incoming_youtube_dl_f, g_yt_playlist, incoming_purge_message_f
from bot.plugins.status_message_fn import (
    status_message_f,
    cancel_message_f,
    exec_message_f,
    upload_document_f,
    upload_log_file
)
from bot.plugins.call_back_button_handler import button
from bot.plugins.custom_thumbnail import (
    save_thumb_nail,
    clear_thumb_nail
)
from bot.helpers.download import down_load_media_f


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    #
    app = Client(
        "LeechBot",
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        workers=343
    )
    #
    incoming_message_handler = MessageHandler(
        incoming_message_f,
        filters=filters.command([f"{LEECH_COMMAND}","{LEECH_COMMAND}{BOT_USERNAME}"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(incoming_message_handler)
    #
    incoming_purge_message_handler = MessageHandler(
        incoming_purge_message_f,
        filters=filters.command([f"purge{BOT_USERNAME}","purge"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(incoming_purge_message_handler)
    #
    incoming_youtube_dl_handler = MessageHandler(
        incoming_youtube_dl_f,
        filters=filters.command([f"{YTDL_COMMAND}","{YTDL_COMMAND}{BOT_USERNAME}"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(incoming_youtube_dl_handler)
    #
    incoming_youtube_playlist_dl_handler = MessageHandler(
        g_yt_playlist,
        filters=filters.command([f"{PYTDL_COMMAND_J}","{PYTDL_COMMAND_J}{BOT_USERNAME}"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(incoming_youtube_playlist_dl_handler)
    #
    status_message_handler = MessageHandler(
        status_message_f,
        filters=filters.command([f"{STATUS_COMMAND}","{STATUS_COMMAND}{BOT_USERNAME}"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(status_message_handler)
    #
    cancel_message_handler = MessageHandler(
        cancel_message_f,
        filters=filters.command([f"{CANCEL_COMMAND_J}","{CANCEL_COMMAND_J}{BOT_USERNAME}"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(cancel_message_handler)
    #
    exec_message_handler = MessageHandler(
        exec_message_f,
        filters=filters.command([f"exec{BOT_USERNAME}","exec"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(exec_message_handler)
    #
    rename_message_handler = MessageHandler(
        rename_message_f,
        filters=filters.command([f"rename{BOT_USERNAME}","rename"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(rename_message_handler)
    #
    upload_document_handler = MessageHandler(
        upload_document_f,
        filters=filters.command([f"upload{BOT_USERNAME}","upload"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(upload_document_handler)
    #
    upload_log_handler = MessageHandler(
        upload_log_file,
        filters=filters.command([f"{LOG_COMMAND}",f"{LOG_COMMAND}{BOT_USERNAME}"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(upload_log_handler)
    #
    help_text_handler = MessageHandler(
        help_message_f,
        filters=filters.command([f"help{BOT_USERNAME}","help"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(help_text_handler)
    #
    new_join_handler = MessageHandler(
        new_join_f,
        filters=~filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(new_join_handler)
    #
    call_back_button_handler = CallbackQueryHandler(
        button
    )
    app.add_handler(call_back_button_handler)
    #
    save_thumb_nail_handler = MessageHandler(
        save_thumb_nail,
        filters=filters.command([f"{SAVE_THUMBNAIL}","{SAVE_THUMBNAIL}{BOT_USERNAME}"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(save_thumb_nail_handler)
    #
    clear_thumb_nail_handler = MessageHandler(
        clear_thumb_nail,
        filters=filters.command([f"{CLEAR_THUMBNAIL}","{CLEAR_THUMBNAIL}{BOT_USERNAME}"]) & filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(clear_thumb_nail_handler)
    #
    app.run()
