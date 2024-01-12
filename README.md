# Device_Tracker
Track your device via telegram bot

## Table of Contents

- [Installation](#installation)
- [Run](#RunProgram)
- [Add script to windows startup](#Add_script_to_windows_startup)

## Installation

1. Run [install.bat](install.bat)
2. Go to [Telegram BotFather](https://telegram.me/BotFather) and create a bot of any name you want
3. Bot father will give you token paste it in [keys.py](/keys.py)
4. Go to [Telegram Bot Raw](https://t.me/RawDataBot) and start
5. you will get a json response like this
    ```json
   {
       "update_id": 123456,
       "message": {
           "message_id": 123456,
           "from": {
               "id": YOUR ID,
               "is_bot": false,
               "first_name": "Jyoti",
               "last_name": "Singh",
               "username": "jyotisingh1980",
               "language_code": "en"
           },
           "chat": {
               "id": YOUR ID,
               "first_name": "yourname",
               "last_name": "name",
               "username": "usname",
               "type": "private"
           },
           "date": 1703230469,
           "text": "/start",
           "entities": [
               {
                   "offset": 0,
                   "length": 6,
                   "type": "bot_command"
               }
           ]
       }
   }
6. copy "YOUR ID" and paste it in [keys.py](/keys.py)
7. Go to [Telegram BotFather](https://telegram.me/BotFather) and set the following commands
   ```bash
    hi - Check bot status
    ss - Get ScreenShot
    img - Get Image of Person
    rec - Record the person
    lock - Lock the windows
    list_and_close_windows - Close any desired open window
    stdown - Shut down windows
    iplocation - Get the IP adress location

## RunProgram
   Open [win.py](win.py)

## Add_script_to_windows_startup
   1. Press `Win + R` to open the Run dialog.
   2. Type `shell:startup` and press Enter. This will open the "Startup" folder.
   3. Create shortcut of [runScriptSilently.vbs](runScriptSilently.vbs) in "Startup" folder
   
