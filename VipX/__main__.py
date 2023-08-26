import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from VipX import LOGGER, app, userbot
from VipX.core.call import Vip
from VipX.plugins import ALL_MODULES
from VipX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("VipX").error(
            "🙄 جلسة بروجرام غير ممتلئة , يرجى ملء جلسة بروجرام الحساب المساعد  😐"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("VipX").warning(
            "🥲😂 معرف سيدي المطور والسر لم يتم ملؤهما .😉 لا تقلق لا مشكلة استمتع بالتوتر مجانا  ، اليسع هنا لا خوفا عليكم🫡🇾🇪"
        )
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
    for all_module in ALL_MODULES:
        importlib.import_module("VipX.plugins." + all_module)
    LOGGER("VipX.plugins").info(
        "😋  تم تحميل كافة الميزات يا حيدي 🇾🇪"
    )
    await userbot.start()
    await Vip.start()
    await Vip.decorators()
    LOGGER("VipX").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️ هيبة الأمبراطـــور اليسع ترعبكم ♨️\n╚═════ஜ۩۞۩ஜ════╝")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("VipX").info("😢 𝐒𝐨𝐫𝐫𝐲 𝐒𝐭𝐨𝐩𝐩𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 ☹️")
