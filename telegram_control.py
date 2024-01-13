import asyncio
from telegram import Bot
from telegram import InputFile
from keys import TOKEN, ID

bot = Bot(token=TOKEN)

def chatID(i):
    return i.message.chat.id
    
async def send_image(image_path, caption, ID):
    image_file = InputFile(open(image_path, 'rb'))
    await bot.send_photo(chat_id=ID, photo=image_file, caption=caption)

async def send_message(message, ID):
    await bot.send_message(chat_id=ID, text=message)

async def send_vid(video_path, caption, ID):
    # Send the video
    video = open(video_path, 'rb')
    await bot.send_video(chat_id=ID, video=video,caption=caption)
    # Close the file
    video.close()



