import telebot
from os import environ

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN'])
# print(bot.token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")