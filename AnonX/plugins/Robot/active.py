from pyrogram import filters
from pyrogram.types import Message

from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS
from AnonX.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(filters.command(ACTIVEVC_COMMAND) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text(
        "𝙂𝙀𝙏𝙏𝙄𝙉𝙂 𝘼𝘾𝙏𝙄𝙑𝙀 𝙑𝙊𝙄𝘾𝙀𝘾𝙃𝘼𝙏𝙎 𝙇𝙄𝙎𝙏𝙎..."
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "𝙋𝙍𝙄𝙑𝘼𝙏𝙀 𝘾𝙃𝘼𝙏𝙎"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("𝙉𝙊 𝘼𝘾𝙏𝙄𝙑𝙀 𝙑𝙊𝙄𝘾𝙀𝘾𝙃𝘼𝙏𝙎 𝙊𝙉 𝙈𝙐𝙎𝙄𝘾𝘽𝙊𝙏...")
    else:
        await mystic.edit_text(
            f"**𝙇𝙄𝙎𝙏 𝙊𝙁 𝘾𝙐𝙍𝙍𝙀𝙉𝙏𝙇𝙔 𝘼𝘾𝙏𝙄𝙑𝙀 𝙑𝙊𝙄𝘾𝙀 𝙊𝙉 𝙈𝙐𝙎𝙄𝘾𝘽𝙊𝙏:-**\n\n{text}",
            disable_web_page_preview=True,
        )


