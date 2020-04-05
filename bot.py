import telebot
import random
from os import environ

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN'])

bot_text = '''
Bienvenido, este bot fue programado por Angel Garcia( @angelgarciablog ) para @whatsapp_beta'''

reglas = "❗❗ *REGLAS* ❗❗❗✅\n\nEnlaces no spam\n✅ Archivos sin virus\n❗❗Respetar a los miembros del grupo❗❗\n\n🚫 No porno, cp, gore, y similares\n🚫 Virus\n🚫 Cadenas con información falsa\n🚫 Molestar al privado\n\nCualquier incumplimiento es motivo de expulsion permanente"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, bot_text)

@bot.message_handler(commands=['reglas'])
def reglas_grupos(message):
  bot.reply_to(message, reglas)

  
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  cid = message.chat.id
  holas="hola","hl, mucho gusto","hola tanto tiempo sin verte", "hl, dime te puedo ayudar en algo?","hooola que tal tu dia"
  if message.text.lower() == "hola" or "hla" or "hl":
    bot.send_message( cid, random.choice(holas))
  buen_dia="buen dia que la pases bien","buen dia","buen dia precioso(a)","que dios bendiga tu dia"
  if message.text.lower() == "buenos dias" or "buen dia":
    bot.send_message(cid, random.choice(buen_dia))
  
bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))
