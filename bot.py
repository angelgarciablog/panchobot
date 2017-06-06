import telebot
from os import environ

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN'])
# print(bot.token)

bot_text = "Howdy, how are you doing?\nSource code on https://glitch.com/~telegram-bot-python"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, bot_text)
  
bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))