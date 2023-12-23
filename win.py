print('Importing Modules...')
from telegram.ext import *
from telegram.ext import filters
import telegram_control
import img
import ctypes
import asyncio
import geocoder
from keys import TOKEN, ID
print('Imported the Modules')

async def response(i,g):
    await telegram_control.send_message(message="Hello!")
    

async def getSS(i,g):
    await telegram_control.send_image(img.take_screenshot(),"The screen shot")

async def whoIsOnMyPC(i,g):
    await telegram_control.send_image(img.cameraCapture(),"This is it")

async def lockWindows(i,g):
    await telegram_control.send_message(message="Locked The Windows")
    # Define necessary constants
    SW_RESTORE = 9
    SPI_SETSCREENSAVEACTIVE = 17
    # Lock the workstation (simulating Win + L)
    ctypes.windll.user32.LockWorkStation()
    # Optionally, disable screensaver to keep the system from locking again
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETSCREENSAVEACTIVE, 0, ctypes.c_void_p(), 0)
    

async def shutdownWindows(i,g):
    await telegram_control.send_message(message="Shutting Windows down")
    # Define necessary constants
    EWX_SHUTDOWN = 1
    EWX_FORCE = 4
    # Shut down Windows
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "shutdown", "/s /t 0", None, 1)
    
async def recordNsend(i,g):
    await telegram_control.send_message(message="Recording the 10sec video") 
    vid = await img.record(12)   
    await telegram_control.send_vid(vid,"Here is a 10 sec video")

async def loc(i,g):
    # Get the device's location
    device_location = geocoder.ip('me').latlng
    print(geocoder.ip('me'))
    if device_location:
        latitude, longitude = device_location
        print(f"Device Location: Latitude {latitude}, Longitude {longitude}")

        # Generate a Google Maps link
        await telegram_control.send_message(message= f"https://www.google.com/maps?q={latitude},{longitude}")
    else:
        await telegram_control.send_message(message="Error in getting the location")    

if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()

    # Commands
    application.add_handler(CommandHandler('hi', response))
    application.add_handler(CommandHandler('ss', getSS))
    application.add_handler(CommandHandler('img', whoIsOnMyPC))
    application.add_handler(CommandHandler('rec', recordNsend))
    application.add_handler(CommandHandler('lock', lockWindows))
    application.add_handler(CommandHandler('stdown', shutdownWindows))
    application.add_handler(CommandHandler('iplocation', loc))
    
    # telegram_control.send_vid("output.avi","Here is a 10 sec video")
    # Run bot
    print('The bot is running')
    application.run_polling()