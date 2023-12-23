# Device_Tracker
Track your device via telegram bot

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Install the required library from requirments.txt.
   ```bash
   pip install -r requirements.txt
2. Go to [Telegram BotFather](https://telegram.me/BotFather) and create a bot of any name you want
3. Bot father will give you token paste it in [keys.py](/keys.py)
4. Go to [Telegram Bot Raw](https://t.me/RawDataBot) and start
5. you will get a json response like this
 ```bash
{
    "update_id": somenumber,
    "message": {
        "message_id": somenumber,
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

