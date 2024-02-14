from pyrogram import Client, filters
import requests
import config
from EQUROBOT import app

# Deep AI API endpoint
DEEP_AI_API_URL = "https://api.deepai.org/api/text-generator"

# Your Deep AI API key
DEEP_AI_API_KEY = config.DEEP_API
# Function to handle incoming messages
@app.on_message(filters.private)
async def chatbot(_, message):
    # Check if the message is from a user
    if message.from_user is not None:
        # Call Deep AI API to generate a response
        headers = {"Api-Key": DEEP_AI_API_KEY}
        params = {"text": message.text}
        response = requests.post(DEEP_AI_API_URL, headers=headers, data=params)
        
        if response.status_code == 200:
            # Extract the generated response from the API
            response_text = response.json()["output"]
            await message.reply(response_text)
        else:
            await message.reply("Sorry, there was an error processing your request.")




# ---------------------------
@app.on_message(filters.command("alive", prefixes="."))
def alive(_, message):
    message.reply_text("I'm alive and kicking!")
