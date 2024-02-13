from pyrogram import Client, filters
from EQUROBOT import app
# ---------------------------
@app.on_message(filters.command("alive", prefixes="."))
def alive(_, message):
    message.reply_text("I'm alive and kicking!")
