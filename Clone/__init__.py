import os
import logging
from pyrogram import Client
import time


FORMAT = "[Cloner]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
                                                    logging.StreamHandler()], format=FORMAT)

# Set up logging
logger = logging.getLogger(__name__)

# For Ping Cmd
StartTime = time.time()


# Set up bot configurations
API_ID = 25629197
API_HASH = "fd41f8bacda97ab0a3ad120b30339978"
TOKEN = "6528046179:AAHkcHbalYrhZjD4rjDXVagtYY1hiSK34zE"

#PYROGRAM BOT CLIENT
bot = Client(name="CloneBot", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Clone.Examples"))
