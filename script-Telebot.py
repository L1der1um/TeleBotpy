#pip install telebot
#pip3 install telebot

from telebot import TeleBot

BOT_TOKEN = 'SUA API KEY'

bot = TeleBot (BOT_TOKEN)

@bot.message_handler(commands=['start', 'olá'])
def send_welcome(message):
    bot.reply_to(message, "MSG BOT")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()