import telebot
import random
from os import environ

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN'])

bot_text = '''
Bienvenido, este bot fue programado por Angel Garcia( @angelgarciablog ) para @whatsapp_beta'''

reglas = "❗❗ *REGLAS* ❗❗❗✅\n\nEnlaces no spam\n✅ Archivos sin virus\n❗❗Respetar a los miembros del grupo❗❗\n\n🚫 No porno, cp, gore, y similares\n🚫 Virus\n🚫 Cadenas con información falsa\n🚫 Molestar al privado\nNo jugar con los comandos del bot\n\nCualquier incumplimiento es motivo de expulsion permanente"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, bot_text)

@bot.message_handler(commands=['reglas'])
def reglas_grupos(message):
  bot.reply_to(message, reglas)


@bot.message_handler(commands=['id'])
def miid(message):
  cid = message.chat.id     
  nombreUsuario = message.from_user.username  
  idUsuario = message.from_user
  bot.reply_to(message, "chat id " + str(cid))
  
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  cid = message.chat.id
  idgrupo = 1001409931709
  miid = 530270550
  if  message.text.lower().startswith('bot di') and cid == miid :                 
    mensaje=message.text                              
    respuesta = ' '.join(mensaje.split(" ")[2:])   
    bot.send_message(idgrupo, respuesta)  





  

@bot.message_handler(func=lambda message: True)            
def echo_message(message):
    cid = message.chat.id
    holas = "hola","hl, mucho gusto","hola tanto tiempo sin verte", "hl, dime te puedo ayudar en algo?","hooola que tal tu dia"
    buen_dia="buen dia que la pases bien","buen dia","buen dia precioso(a)","que dios bendiga tu dia"
    mt = message.text.lower()
    if mt == "hola" or mt == "hl" or mt == "hla":
      bot.send_message( cid, random.choice(holas))
    if mt == "buenos dias" or mt == "buen dia" or mt == "hola buenos dias" or mt == "hola buenos dias":
      bot.send_message( cid, random.choice(buen_dia))


    
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
            bienvenida = "Bienvenido a "         
            bienvenida += str(cname)                   
            bienvenida += "  "
    else:                                              
        nun = m.new_chat_member.username               
        bienvenida = "Bienvenido a "            
        bienvenida += str(cname)                      
        bienvenida += " @"

    bot.send_message(cid, str(bienvenida) + str(nun)+"  por favor lee las reglas usando el comando /reglas")

  
bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))
