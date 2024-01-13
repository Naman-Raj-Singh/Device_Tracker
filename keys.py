# keys.py

import ctypes

# Replace 'YOUR_BOT_TOKEN' with the token obtained from BotFather
TOKEN = 'YOUR_BOT_TOKEN'

# Replace 'USER_CHAT_ID' with the chat ID of the user or group where you want to send the image
ID = 'USER_CHAT_ID'

# Check if the TOKEN is set to 'not_rolled'
if TOKEN == 'YOUR_BOT_TOKEN':
    ctypes.windll.user32.MessageBoxW(0, "Bot token has not been provided. Please update the TOKEN in keys.py.", "Token Not provided", 1)
    exit()
