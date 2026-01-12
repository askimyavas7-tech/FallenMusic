# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

import asyncio
import importlib
import os

from pyrogram import idle

from FallenMusic import (
    ASS_ID,
    ASS_NAME,
    ASS_USERNAME,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    SUNAME,
    app,
    app2,
    pytgcalls,
)
from FallenMusic.Modules import ALL_MODULES


async def fallen_startup():
    # Load modules
    LOGGER.info("[•] Loading Modules...")
    for module in ALL_MODULES:
        importlib.import_module("FallenMusic.Modules." + module)
    LOGGER.info(f"[•] Loaded {len(ALL_MODULES)} Modules.")

    # Prepare directories
    LOGGER.info("[•] Refreshing Directories...")
    if not os.path.isdir("downloads"):
        os.mkdir("downloads")
    if not os.path.isdir("cache"):
        os.mkdir("cache")
    LOGGER.info("[•] Directories Refreshed.")

    # Send bot info
    try:
        await app.send_message(
            SUNAME,
            f"🔸 𝙏𝙍𝙀𝙉𝘿𝙔𝙊𝙇 𝙈𝙐̈𝙕𝙄𝙆 𝘽𝙊𝙏 🔸\n\n"
            f"𖢵 ɪᴅ : `{BOT_ID}`\n"
            f"𖢵 ɴᴀᴍᴇ : {BOT_NAME}\n"
            f"𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{BOT_USERNAME}",
        )
    except Exception as e:
        LOGGER.error(
            f"Trendyol Müzik Bot failed to send message at @{SUNAME}: {e}"
        )

    # Send assistant info
    try:
        await app2.send_message(
            SUNAME,
            f"🔸 𝙏𝙍𝙀𝙉𝘿𝙔𝙊𝙇 𝙈Ü𝙕𝙄𝙆 𝘼𝙎𝙄𝙎𝙏𝘼𝙉 🔸\n\n"
            f"𖢵 ɪᴅ : `{ASS_ID}`\n"
            f"𖢵 ɴᴀᴍᴇ : {ASS_NAME}\n"
            f"𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{ASS_USERNAME}",
        )
    except Exception as e:
        LOGGER.error(
            f"Trendyol Müzik Asistan failed to send message at @{SUNAME}: {e}"
        )

    # Trigger /start
    try:
        await app2.send_message(BOT_USERNAME, "/start")
    except Exception:
        pass

    LOGGER.info("[•] Bot Started As 🔸 Trendyol Müzik Bot 🔸")
    LOGGER.info("[•] Assistant Started As 🔸 Trendyol Müzik Asistan 🔸")

    # Start PyTgCalls (SAFE MODE)
    LOGGER.info("[•] Starting PyTgCalls Client...")

    try:
        await pytgcalls.start()
        LOGGER.info("[✓] PyTgCalls Started Successfully.")
    except Exception as e:
        LOGGER.error(
            f"[!] PyTgCalls Disabled (NodeJS missing or unsupported): {e}"
        )

    # Keep bot alive
    await idle()


if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(fallen_startup())
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        LOGGER.error("Trendyol Müzik Bot Stopped.")
