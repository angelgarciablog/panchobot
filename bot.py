import telebot
from os import environ

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN'])

bot_text = '''
Howdy, how are you doing?
Source code on https://glitch.com/~{}
'''.format(environ['PROJECT_NAME'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, bot_text)

bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))

@bot.message_handler(func=lambda message: True)
def echo_message(message):
  cid = message.chat.id
  if message.text.lower() == "hola":
    bot.send_message( cid, '@bot.message_handler(func=lambda message: True)
def echo_message(message):
  cid = message.chat.id
  if message.text.lower() == "hola":
    bot.send_message( cid, 'hola,amigo'

