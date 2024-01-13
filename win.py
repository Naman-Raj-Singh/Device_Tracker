print("Importing Modules...")

from telegram.ext import (
    Updater,
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    CallbackContext,
    filters,
)
import telegram_control
from telegram_control import chatID
import ctypes, geocoder, img
from keys import TOKEN
import pygetwindow as gw
from os import system

print("Starting a bot....")
windows = gw.getAllTitles()


def echo(i, g):
    text_content = i.message.text


async def close_a_window(i, g):
    windows = gw.getAllTitles()
    # mydfe_value = context.user_data.get('mywin', "Default Value")
    index_to_close = int(i.message.text)

    if 0 < index_to_close <= len(windows):
        # Close the selected window
        gw.getWindowsWithTitle(windows[index_to_close - 1])[0].close()
        await telegram_control.send_message(
            message=f"Closed window with index {index_to_close}.", ID=chatID(i)
        )
    elif index_to_close == 0:
        await telegram_control.send_message(message="Operation canceled.", ID=chatID(i))
    else:
        await telegram_control.send_message(
            message="Invalid index. No window closed.", ID=chatID(i)
        )

    return ConversationHandler.END


async def list_and_close_windows(i, g):
    # Get a list of all open windows
    windows = gw.getAllTitles()

    if windows:
        await telegram_control.send_message(message="Open Windows:", ID=chatID(i))
        for num, window_title in enumerate(windows, 1):
            if window_title.strip():  # Check if the title is not an empty string
                await telegram_control.send_message(
                    message=f"{num}. {window_title}", ID=chatID(i)
                )
        await telegram_control.send_message(
            message="Enter the index of the window to close (0 to cancel): ",
            ID=chatID(i),
        )
    return RECEIVING_CHOICE


async def response(i, g):
    await telegram_control.send_message(message="Hello!", ID=chatID(i))


async def getSS(i, g):
    await telegram_control.send_image(
        img.take_screenshot(), "The screen shot", ID=chatID(i)
    )


async def whoIsOnMyPC(i, g):
    await telegram_control.send_image(img.cameraCapture(), "This is it", ID=chatID(i))


async def lockWindows(i, g):
    await telegram_control.send_message(message="Locked The Windows", ID=chatID(i))

    system("rundll32.exe user32.dll,LockWorkStation")


async def shutdownWindows(i, g):
    await telegram_control.send_message(message="Shutting Windows down", ID=chatID(i))
    system("shutdown /s /t 1")


async def recordNsend(i, g):
    await telegram_control.send_message(
        message="Recording the 10sec video", ID=chatID(i)
    )
    vid = await img.record(12)
    await telegram_control.send_vid(vid, "Here is a 10 sec video", ID=chatID(i))


async def loc(i, g):
    # Get the device's location
    device_location = geocoder.ip("me").latlng
    print(geocoder.ip("me"))
    if device_location:
        latitude, longitude = device_location
        print(f"Device Location: Latitude {latitude}, Longitude {longitude}")
        # Generate a Google Maps link
        await telegram_control.send_message(
            message=f"https://www.google.com/maps?q={latitude},{longitude}",
            ID=chatID(i),
        )
    else:
        await telegram_control.send_message(
            message="Error in getting the location", ID=chatID(i)
        )


if __name__ == "__main__":
    application = Application.builder().token(TOKEN).build()
    # Create a conversation handler with two states
    CHOOSING, RECEIVING_CHOICE = range(2)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("list_and_close_windows", list_and_close_windows)],
        states={
            CHOOSING: [],
            RECEIVING_CHOICE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, close_a_window)
            ],
        },
        fallbacks=[],
    )
    # Commands
    application.add_handler(CommandHandler("hi", response))
    application.add_handler(CommandHandler("ss", getSS))
    application.add_handler(CommandHandler("img", whoIsOnMyPC))
    application.add_handler(CommandHandler("rec", recordNsend))
    application.add_handler(CommandHandler("lock", lockWindows))
    application.add_handler(CommandHandler("stdown", shutdownWindows))
    application.add_handler(CommandHandler("iplocation", loc))
    application.add_handler(conv_handler)
    # Run bot
    print("BOT IS STARTED")
    application.run_polling(5)  # This delays bot by 5 seconds
