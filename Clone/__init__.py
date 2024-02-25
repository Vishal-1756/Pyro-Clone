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
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TOKEN = os.getenv("TOKEN")

#PYROGRAM BOT CLIENT
bot = Client(name="CloneBot", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Clone"))
