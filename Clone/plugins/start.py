from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
import time 
from Clone import StartTime

@Client.on_message(filters.private & filters.command("start"))
async def start(client: Client, message: Message):
  await message.reply("Hey! It's Just a Cloner Bot example source Code")
  
@Client.on_message(filters.command(["ping"]))
async def ping_pong(client: Client, message: Message):
    start_time = time.time()
    msg =  await message.reply_text("Checking Services...✅")
    await msg.edit("Pinging Baby 🐥...")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = get_readable_time((time.time() - StartTime))
    await msg.edit(f"**Service Ping Stats**\n⋙ 🎯 **Ping**: {ping_time}\n⋙ ⬆️ **Service Uptime**: {uptime}")
    try:
        await message.delete()
    except:
        return
