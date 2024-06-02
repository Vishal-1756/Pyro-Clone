import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from Clone import bot
from Clone import API_ID, API_HASH
import pyrogram

@bot.on_message(filters.private & filters.command("bclone"))
async def bot_clone(bot: Client, msg: Message):
    chat = msg.chat
    cmd = msg.command
    user_id = msg.from_user.id
    try:
        TOKEN = msg.text.split()[1]
    except IndexError:
        await msg.reply("Please provide a valid BOT_TOKEN.\nUsage:\n\n /bclone BOT_TOKEN")
        return

    text = await msg.reply("Booting Your Client")
    
    async def start_new_client():
        client_name = f":memory:{user_id}"
        try:
            client = Client(client_name, API_ID, API_HASH, bot_token=TOKEN, plugins={"root": "Clone"})
            await client.start()
            user = await client.get_me()
            await text.edit(f"Booted Client as @{user.username} Do /ping for testing")        
            await msg.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\n Use Help For Help Menu\n\nThanks for Cloning.\n **ignore this message its happened due to over load**")
            await pyrogram.idle()
        except Exception as e:
            await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

    asyncio.create_task(start_new_client())

