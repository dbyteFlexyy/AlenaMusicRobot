# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


import asyncio
import importlib
from pyrogram import idle
from pyrogram.types import BotCommand
from pytgcalls.exceptions import NoActiveGroupCall
import config
from ShrutiMusic import LOGGER, app, userbot
from ShrutiMusic.core.call import Nand
from ShrutiMusic.misc import sudo
from ShrutiMusic.plugins import ALL_MODULES
from ShrutiMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

# Bot Commands List
COMMANDS = [
    BotCommand("start", "sᴛᴀʀᴛ ᴍᴇ ʙᴀʙʏ 💗"),
    BotCommand("help", "ʜᴇʟᴘ ᴋʀᴅᴜ ꜱᴡᴇᴇᴛʏ 🌷"),
    BotCommand("ping", "ᴘɪɴɢ ᴍʏ ʜᴇᴀʀᴛ 💞"),
    BotCommand("play", "ᴍᴜꜱɪᴄ ᴄʜᴀʟᴀᴅᴏ ʙᴀʙʏ 🎀"),
    BotCommand("vplay", "ᴠɪᴅᴇᴏ ᴘʟᴀʏ ᴅᴀʀʟɪɴɢ 📺💘"),
    BotCommand("playrtmps", "ʟɪᴠᴇ ᴠɪᴅᴇᴏ ᴅᴏʟʟ 🌸"),
    BotCommand("playforce", "ꜰᴏʀᴄᴇ ᴀᴜᴅɪᴏ ᴍʏ ᴄᴜᴛɪᴇ 🎧💕"),
    BotCommand("vplayforce", "ꜰᴏʀᴄᴇ ᴠɪᴅᴇᴏ ᴍʏ ᴀɴɢᴇʟ 📺✨"),
    BotCommand("pause", "ᴘᴀᴜꜱᴇ ᴋᴀʀ ᴊᴀɴᴇᴍᴀɴ 💞"),
    BotCommand("resume", "ᴡᴀᴘᴀꜱ ᴄʜᴀʟᴀᴅᴏ ᴍᴇʀɪ ʙᴀʙʏ 🌷"),
    BotCommand("skip", "ɴᴇꜱᴛ ᴋᴀʀᴏ ᴄᴜᴛᴇ ᴘɪᴇ 🍰💗"),
    BotCommand("end", "ᴇɴᴅ ᴋʀᴅᴏ ᴍᴇʀɪ ʙᴀʙʏ 💋"),
    BotCommand("stop", "ꜱᴛᴏᴘ ᴋʀᴅᴏ ꜱᴡᴇᴇᴛʜᴇᴀʀᴛ 💞"),
    BotCommand("queue", "ǫᴜᴇᴜᴇ ᴅɪᴋʜᴀᴏ ᴍʏ ᴅᴏʟʟ 🎀"),
    BotCommand("auth", "ᴀᴅᴅ ʙᴀʙʏ ɪɴ ʟɪꜱᴛ 💗"),
    BotCommand("unauth", "ʀᴇᴍᴏᴠᴇ ʙᴀʙʏ ғʀᴏᴍ ʟɪꜱᴛ 💔"),
    BotCommand("authusers", "ᴍʏ ᴀɴɢᴇʟꜱ ʟɪꜱᴛ 👼💞"),
    BotCommand("cplay", "ᴄʜᴀɴɴᴇʟ ᴀᴜᴅɪᴏ ᴍʏ ʙᴀʙʏ 🎧🌸"),
    BotCommand("cvplay", "ᴄʜᴀɴɴᴇʟ ᴠɪᴅᴇᴏ ʙᴀʙʏ 📺💗"),
    BotCommand("cplayforce", "ꜰᴏʀᴄᴇ ᴄʜᴀɴɴᴇʟ ᴀᴜᴅɪᴏ 💕"),
    BotCommand("cvplayforce", "ꜰᴏʀᴄᴇ ᴄʜᴀɴɴᴇʟ ᴠɪᴅᴇᴏ 🌸"),
    BotCommand("channelplay", "ɢʀᴏᴜᴘ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴍʏ ᴀɴɢᴇʟ 💞"),
    BotCommand("loop", "ʟᴏᴏᴘ ᴏɴ/ᴏꜰꜰ ᴍʏ ʟᴏᴠᴇ 💗"),
    BotCommand("stats", "ʙᴏᴛ ꜱᴛᴀᴛꜱ ᴄᴜᴛɪᴇ 📊💞"),
    BotCommand("shuffle", "ꜱʜᴜꜰꜰʟᴇ ᴅʀᴇᴀᴍꜱ ʙᴀʙʏ 🌙💗"),
    BotCommand("seek", "ꜱᴇᴇᴋ ꜰᴏʀᴡᴀʀᴅ ᴀɴɢᴇʟ ➡️💕"),
    BotCommand("seekback", "ꜱᴇᴇᴋ ʙᴀᴄᴋ ꜱᴡᴇᴇᴛʏ ⬅️🌸"),
    BotCommand("song", "ᴍᴘ3/ᴍᴘ4 ʟᴏᴀᴅ ᴍʏ ʙᴀʙʏ 🎶💗"),
    BotCommand("speed", "ᴀᴜᴅɪᴏ ꜱᴘᴇᴇᴅ ᴄᴜᴛɪᴇ ⚡💞"),
    BotCommand("cspeed", "ᴄʜᴀɴɴᴇʟ ꜱᴘᴇᴇᴅ ꜱᴡᴇᴇᴛʜᴇᴀʀᴛ 🎀"),
    BotCommand("tagall", "ᴛᴀɢ ᴇᴠᴇʀʏᴏɴᴇ ᴍʏ ᴅᴏʟʟ 💗"),
]

async def setup_bot_commands():
    """Setup bot commands during startup"""
    try:
        # Set bot commands
        await app.set_bot_commands(COMMANDS)
        LOGGER("ShrutiMusic").info("Bot commands set successfully!")
        
    except Exception as e:
        LOGGER("ShrutiMusic").error(f"Failed to set bot commands: {str(e)}")

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await app.start()
    
    # Setup bot commands during startup
    await setup_bot_commands()

    for all_module in ALL_MODULES:
        importlib.import_module("ShrutiMusic.plugins" + all_module)

    LOGGER("ShrutiMusic.plugins").info("Successfully Imported Modules...")

    await userbot.start()
    await Nand.start()

    try:
        await Nand.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ShrutiMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass

    await Nand.decorators()

    LOGGER("ShrutiMusic").info(
        "\x53\x68\x72\x75\x74\x69\x20\x4d\x75\x73\x69\x63\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\x0a\x0a\x44\x6f\x6e\x27\x74\x20\x66\x6f\x72\x67\x65\x74\x20\x74\x6f\x20\x76\x69\x73\x69\x74\x20\x40\x53\x68\x72\x75\x74\x69\x42\x6f\x74\x73"
    )

    await idle()

    await app.stop()
    await userbot.stop()
    LOGGER("ShrutiMusic").info("Stopping Shruti Music Bot...🥺")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 
