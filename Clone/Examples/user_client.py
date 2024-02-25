import os
from pyrogram import Client, filters
from pyrogram.types import Message
from Clone import bot
from Clone import API_ID, API_HASH
import pyrogram

@bot.on_message(filters.private & filters.command("uclone"))
async def user_clone(bot: bot, msg: Message):
    chat = msg.chat
    cmd = msg.command
    try:
        SESSION = msg.text.split()[1]
    except IndexError:
        await msg.reply("Please provide a valid session string.\nUsage:\n\n /clone session")
        return

    text = await msg.reply("Booting Your Client")
    
    try:        
        # Change your root directory here
        client = Client(":memory:", API_ID, API_HASH, session_string=SESSION, plugins={"root": "Clone"})
        await client.start()
        await pyrogram.idle()
        user = await client.get_me()
        await text.edit(f"Booted Client as @{user.username} Do /ping Or .ping for testing")        
        await msg.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\n Use Help For Help Menu\n\nThanks for Cloning.\n **ignore this message its happened due to over load**")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
