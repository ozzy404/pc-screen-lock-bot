import telebot
import os
from telebot import types

# Enter your Telegram Bot token here
TOKEN = 'YOUR_BOT_TOKEN_HERE'
# Replace with your Telegram user ID
ALLOWED_USER_ID = YOUR_TELEGRAM_USER_ID_HERE

bot = telebot.TeleBot(TOKEN)

def block_screen():
    os.system("rundll32.exe user32.dll, LockWorkStation")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id == ALLOWED_USER_ID:
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_block = types.KeyboardButton('Lock Screen')
        markup.add(btn_block)
        bot.send_message(message.chat.id, "Welcome! Press the button below to lock the screen.", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "You don't have access to this command.")

@bot.message_handler(func=lambda message: message.text == "Lock Screen")
def handle_block_screen(message):
    if message.from_user.id == ALLOWED_USER_ID:
        block_screen()
        bot.send_message(message.chat.id, "Screen successfully locked!")
    else:
        bot.send_message(message.chat.id, "You don't have access to this command.")

bot.polling()
