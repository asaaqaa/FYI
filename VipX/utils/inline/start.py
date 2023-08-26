from typing import Union
import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import GROUP_USERNAME, CHANNEL_USERNAME


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="•─╼⃝𖠁مجموعتگ◈الى◈أضفني 𖠁⃝╾─•",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋المميزات🦋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙️اعدادات⚙️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons

#extra shit
BOT_USERNAME = ("{BOT_USERNAME}")

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    global GROUP_USERNAME
    global CHANNEL_USERNAME
    buttons = [
        [
            InlineKeyboardButton(
                text="•─╼⃝𖠁مجموعتگ◈الى◈أضفني 𖠁⃝╾─•",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="۞ أوامر التشغيل ۞", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="قناة السورس�", url=f"https://t.me/{CHANNEL_USERNAME}",
            ),
        
            InlineKeyboardButton(
                text="جروب الدعم✨", url=f"https://t.me/{GROUP_USERNAME}",
            ),
        ],
     ]
    return buttons
