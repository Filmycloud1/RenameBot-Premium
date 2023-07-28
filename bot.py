import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6419833706:AAGkIo2vhOpbhQZtWsgyGoFUaHMoaBEwyOA")

API_ID = int(os.environ.get("API_ID", "28189122"))

API_HASH = os.environ.get("API_HASH", "1ebf75b3d12e23c93a79dab2aceb6eea")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
