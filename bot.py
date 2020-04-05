import telebot
import random
from os import environ

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN'])

bot_text = '''
Bienvenido, este bot fue programado por Angel Garcia( @angelgarciablog ) para @whatsapp_beta'''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, bot_text)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
  cid = message.chat.id
  holas="hola","hl, mucho gusto","hola tanto tiempo sin verte", "hl, dime te puedo ayudar en algo?","hooola que tal tu dia"
  if message.text.lower() == "hola" or "hla" or "hl":
    bot.send_message( cid, random.choice(holas))
  
@bot.message_handler(commands=["reglas"])
def reglas(message):
  bot.reply_to(message, "❗❗❗ *REGLAS* ❗❗❗\n
✅ Enlaces no spam\n
✅ Archivos sin virus\n
❗❗Respetar a los miembros del grupo❗❗\n
No porno, cp, gore, y similares \n
🚫 Virus\n
🚫 Cadenas con información falsa\n
🚫 Molestar al privado")

bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))
