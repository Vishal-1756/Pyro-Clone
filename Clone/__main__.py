import pyrogram
from Clone import bot

async def run_clients():
      await bot.start()
      
if __name__ == "__main__":
    bot.loop.run_until_complete(run_clients())
