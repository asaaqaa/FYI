

from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VipX import app
import string
from strings import get_command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

SHAYRI = [ " 🌺**‏أستغفر الله العظيم واتوب اليه 🤍**🌺 \n\n**🥀‏أستغفر الله العظيم واتوب اليه 🤍.🥀** ",
           " 🌺**♡نَحنُ نَرزُقُكَ♡

‏شيءٌ تكفَّل الله به، فلِمَ تقلق بشأنه !**🌺 \n\n**🥀﴿ نَحنُ نَرزُقُكَ ﴾​​

‏شيءٌ تكفَّل الله به، فلِمَ تقلق بشأنه !.🥀** ",
           " 🌺**" لَا تَخَفْ وَلَا تَحْزَنْ ۖ إِنَّا مُنَجُّوكَ ."🤍।**🌺 \n\n**🥀**" لَا تَخَفْ وَلَا تَحْزَنْ ۖ إِنَّا مُنَجُّوكَ ."🤍.🥀** ",
           " 🌺**"بالغ في حُسن ظنِّك بالله، فإن جزاء حُسن الظَّن أن تنال ما ظَنَنْت."।**🌺 \n\n**🥀"بالغ في حُسن ظنِّك بالله، فإن جزاء حُسن الظَّن أن تنال ما ظَنَنْت.".🥀** " ] 
           
# Command
SHAYRI_COMMAND = get_command("SHAYRI_COMMAND")

@app.on_message(
    filters.command(["SHAYRI_COMMAND"]) | filters.command(["اليسع","مطور","سورس"],prefixes= ["/", "!","","#"])
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHAYRI),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨الدعم✨", url=f"https://t.me/ASAAQLIO"),
                    InlineKeyboardButton(
                        "✨قناة السورس✨", url=f"https://t.me/Mlze1bot")
                    
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(["SHAYRI_COMMAND"]) | filters.command(["اليسع","مطور","سورس"],prefixes= ["/", "!","","#"])
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHAYRI),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨الدعم✨", url=f"https://t.me/ASAAQLIO"),
                    InlineKeyboardButton(
                        "✨قناة السورس✨", url=f"https://t.me/Mlze1bot")
                    
                ]
            ]
        ),
)
