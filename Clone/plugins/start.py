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
    start_time = StartTime
    lol = await message.reply_text('Pong!')
    end_time = time.time()
    elapsed_time = round((end_time - start_time) * 1000, 3)
    await lol.edit_text(f'Pong! {elapsed_time}ms')
