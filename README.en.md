# Telegram Screen Lock Bot

This project demonstrates the code for a Telegram bot that allows you to remotely lock the screen of your computer.<br>
[![YouTube](https://img.shields.io/badge/YouTube-Video-red?logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Telegram Bots

- [BotFather](https://t.me/botfather) - For creating and managing Telegram bots.
- [userinfobot](https://t.me/userinfobot) - For getting your Telegram ID.

## Requirements

Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

1. **Clone the repository:**

   Copy the repository URL and run the command:

   ```bash
   git clone https://github.com/ozzy404/pc-screen-lock-bot.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd pc-screen-lock-bot
   ```

3. **Install the required libraries:**

   Ensure that Python is installed. Use the `requirements.txt` file to install the required libraries. Run the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Creating a Telegram Bot:**

   - Open Telegram and find [BotFather](https://t.me/botfather).
   - Send the `/start` command to begin.
   - Create a new bot using the `/newbot` command and follow the instructions.
   - Copy the token you receive and paste it into the `bot_script.py` file.

2. **Getting Your Telegram ID:**

   - Find [userinfobot](https://t.me/userinfobot) on Telegram.
   - Send the `/start` command to get your ID.
   - Copy the ID and paste it into the `bot_script.py` file.

3. **Setting Up Autostart:**

   1. **Creating an .exe File:**

      - In the directory with your script, run the following command to create an `.exe` file:
        ```bash
        pyinstaller --onefile --windowed bot_script.py
        ```
      - After running this command, the `.exe` file will appear in the `dist` folder.

   2. **Adding to Autostart:**

      - Open `Win + R`, type `shell:startup`, and press Enter.
      - Copy the `.exe` file into the opened startup folder.
      - Now, your bot will start automatically when the system boots.

## Available Documentation Versions

- [English Version](README.en.md)
- [Russian Version](README.ru.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
