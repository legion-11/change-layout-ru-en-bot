from time import sleep
import telebot
from telebot.types import Message
from config import Config
from app.functions import translate


bot = telebot.TeleBot(Config.TOKEN, threaded=False, skip_pending=True)
bot.remove_webhook()
sleep(1)
bot.set_webhook(url=Config.HOST_URL)


@bot.message_handler(commands=['start'])
def handle_help(message: Message):
    text_message = "Привет! Это бот для перевода текста написаного в " \
                   "другой раскладке (с руского на английкий и английского на руский)"

    bot.send_message(message.chat.id, text_message)


@bot.message_handler(commands=["fix"])
def reply_message(message: Message):
    print(message.json)
    bot.send_message(message.chat.id,
                     translate(message.reply_to_message.text) if message.reply_to_message else "no message")


@bot.message_handler(content_types=["text"])
def dir_message(message: Message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, translate(message.text))
