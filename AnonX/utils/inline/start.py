from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝘽𝘼𝘽𝙔 𝘼𝘿𝘿 𝙈𝙀 𝙄𝙉 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙃𝙀𝙇𝙋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝙎𝙀𝙏𝙏𝙄𝙉𝙂𝙎", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙊𝙒𝙉𝙀𝙍", user_id=OWNER),
            InlineKeyboardButton(
                text="𝙎𝙐𝙋𝙋𝙊𝙍𝙏", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝘽𝘼𝘽𝙔 𝘼𝘿𝘿 𝙈𝙀 𝙄𝙉 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙃𝙀𝙇𝙋", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="𝙊𝙒𝙉𝙀𝙍", user_id=OWNER),
            InlineKeyboardButton(
                text="𝙎𝙐𝙋𝙋𝙊𝙍𝙏", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="𝘼𝘽𝙊𝙐𝙏 𝙊𝙒𝙉𝙀𝙍", url=f"https://t.me/about_aakash"
                )
        ],
     ]
    return buttons
