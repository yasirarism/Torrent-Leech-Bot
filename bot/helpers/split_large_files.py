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


import asyncio
import os
import time
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

from bot import (
    MAX_TG_SPLIT_FILE_SIZE
)


async def split_large_files(input_file):
    working_directory = os.path.dirname(os.path.abspath(input_file))
    new_working_directory = os.path.join(
        working_directory,
        str(time.time())
    )
    # create download directory, if not exist
    if not os.path.isdir(new_working_directory):
        os.makedirs(new_working_directory)
    # if input_file.upper().endswith(("MKV", "MP4", "WEBM", "MP3", "M4A", "FLAC", "WAV")):
    """The below logic is DERPed, so removing temporarily
    """
    # handle normal files here
    o_d_t = os.path.join(
        new_working_directory,
        os.path.basename(input_file)
    )
    o_d_t = f"{o_d_t}."
    file_genertor_command = [
        "split",
        "--numeric-suffixes=1",
        "--suffix-length=5",
        f"--bytes={MAX_TG_SPLIT_FILE_SIZE}",
        input_file,
        o_d_t
    ]
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    return new_working_directory


async def cult_small_video(video_file, out_put_file_name, start_time, end_time):
    file_genertor_command = [
        "ffmpeg",
        "-hide_banner",
        "-i",
        video_file,
        "-ss",
        start_time,
        "-to",
        end_time,
        "-async",
        "1",
        "-strict",
        "-2",
        "-c",
        "copy",
        out_put_file_name
    ]
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    LOGGER.info(t_response)
    return out_put_file_name
