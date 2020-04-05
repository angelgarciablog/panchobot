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
  while message.text.lower() not == "hola":
    holas="hola","hl, mucho gusto","hola tanto tiempo sin verte", "hl, dime te puedo ayudar en algo?","hooola que tal tu dia"
    if message.text.lower() == "hola" or "hla" or "hl":
      bot.send_message( cid, random.choice(holas))

    
@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def command_bienvenida(m):
    cid = m.chat.id                                   
    cname = m.chat.title                              
    bienvenida = ""                                    

    if (m.new_chat_member.username is None):          
        nun = m.new_chat_member.first_name            

        if (m.new_chat_member.last_name is not None): 
            nun += " "                        
            nun += m.new_chat_member.last_name         

        else:                                          
            bienvenida = "Bienvenido al grupo"         
            bienvenida += str(cname)                   
            bienvenida += " "
    else:                                              
        nun = m.new_chat_member.username               
        bienvenida = "Bienvenido al grupo "            
        bienvenida += str(cname)                      
        bienvenida += " @"

    bot.send_message(cid, str(bienvenida) + str(nun))

  
bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))
