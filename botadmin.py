import telebot
import random
import datetime
from os import environ
import time

#comentario de prueva
bot = telebot.TeleBot('716415124:xxxxxxxxx')  # borra lo que esta dentro de las comillas y pega el token generado con botFather.(las comillas no las borres xd)

#bot = telebot.TeleBot(environ['TELEGRAM_TOKEN'])

bot_text = '''
Bienvenido, este bot fue programado por Angel Garcia( @angelgarciablog ) para @whatsapp_beta'''

reglas = "❗❗ *REGLAS* ❗❗❗\n\n✅Enlaces no spam\n✅ Archivos sin virus\n❗❗Respetar a los miembros del grupo❗❗\n\n🚫 No porno, cp, gore, y similares\n🚫 Virus\n🚫 Cadenas con información falsa\n🚫 Molestar al privado\nNo jugar con los comandos del bot\n\nCualquier incumplimiento es motivo de expulsion permanente \n🚫 No jugar con los emoji de telegram  \n🚫No jugar con los comandos de los bot."

ayuda = '     AYUDA    \n\n comandos disponibles: \n /id : Te muestra tu id y la id del chat. \n /miinfo : Te proporciona todos tus datos personales disponibles en la configuracion de telegram. \n /reglas : Te muestra las reglas del grupo whatsapp beta. \n /ayuda o /help : te muestra este msj. \n\n/hora : muestra la hora de algunas regiones (en desarrollo)\n\n MAS : \n    interactua frente algunas frases por ejemplo ante un saludo ”hola" \n ...contruyendo' 

def saludos(n):
    saludo=["Cordiales saludos "+n+" Bienvenido/a al Mejor grupo de Telegram!", "Cómo va "+n+ " bonito nombre","Bienvenid@! "+n , n+" ¿Qué cosa podría hacer para darte la bienvenida?.","Hola "+n+" por fin llegaste!","Saluditos "+n+ " espero te sientas bien en el grupito!","Buenaas "+n+ " , espero que pases bien en este grupito : )","Qué tal "+n+"?","WOOW llegó "+n+", Cuanto tiempo sin verte! Bienvenid@.","Un saludito "+n ,"Hola "+n+" ya me estaba desesperando que no venias!","Por qué me sigues a todos lados "+n+" ? "," Hola "+n+" siento ganas de llorar por que ahora estas conmigo en el mejor grupito!","Ohh my God! "+n+" eres tu, bienvenid@ a la familia.","Uhhh "+n+" te vi en mis sueños, ahora estas aquí, bienvenid@","Hola "+n+" yo sabia que estarías aquí conmigo, la mejor decisión!",n+" Hola, eres la mejor persona del universo! Bienvenid@","No aguantó nuestras tonterías! Un placer "+n]
    return (random.choice(saludo))

@bot.message_handler(commands=['hora'])
def reloj(message):
    lugar="GMT+00:00 hora estándar de Europa occidental"
    dt = datetime.datetime.now()
    bot.reply_to(message,lugar+ "\n\n{}:{}:{}".format( dt.hour, dt.minute, dt.second ) )

@bot.message_handler(commands=['ayuda'])
def ayud(message):
    global ayuda
    cid = message.chat.id
    print(cid)
    bot.send_message(cid, ayuda)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, bot_text)

@bot.message_handler(commands=['reglas'])
def reglas_grupos(message):
    bot.reply_to(message, reglas)

@bot.message_handler(commands=['id'])
def id(message):
    cid = message.chat.id
    idUsuario = message.from_user.id
    bot.reply_to(message, "chat id : " + str(cid) + "\n\n Id Usuario : " + str(idUsuario))
  

  
@bot.message_handler(commands=['miinfo'])
def miinfo(message):
    cid = message.chat.id
    mensaje = 'Datos personales\n\n @{}\n🆔Identidad: {}\n👤Nombre: {}\n🔘Apellido: {}\n🌎Region: {}\n🤖Bot: {}\n '.format(message.from_user.username,message.from_user.id,message.from_user.first_name,message.from_user.last_name,message.from_user.language_code,message.from_user.is_bot)
    bot.reply_to(message, mensaje)



@bot.message_handler(func=lambda message: True)
def echo_message(message):
  cid = message.chat.id
  holas="hola","hl, mucho gusto","hola tanto tiempo sin verte", "hl, dime te puedo ayudar en algo?","hooola que tal tu dia","hola como estas","Hola, que tal tu dia"
  estados="bien gracias","bien y tu","hola bien y tu","super y tu"
  novedades="si detectamos algun cambio lo reportaremos en el canal"
  buendia = "buen dia para ti tambien","buenos dias amigo","como amanesiste?","Buen dia para todos"
  msj = message.text.lower()
  
  #Guardamos en la variale cid el id de el mensaje recibido 
  idUsu = message.from_user.id
  
  if msj ==  "bot vete" :
    
    if idUsu== 530270550:
      bot.send_message(cid, 'vale :C, adios mi gente!')	
      bot.leave_chat(cid)
  
  if msj in ["hola","hla","hello","hl"]:
      bot.send_chat_action(cid, 'typing') # Enviando ...
      time.sleep(1) #La respuesta del bot tarda 1 segundo en ejecutarse
      bot.send_message( cid, random.choice(holas))
   
  if msj in ["cm estan","como estan","como estan amigos","hola como estan","que tal amigos"]:
    bot.send_message( cid, random.choice(estados))
    
   
  if msj in ["que hay de nuevo","que de nuevo","que trae","que novedades"]:
    bot.send_message( cid, novedades)
    
  if msj in ["Buenos días","buen dia","buen dia grupo"]:
    bot.send_message(cid, random.choice(buendia))
    
  if  message.text.lower().startswith('bot di'): 
    if cid == 530270550 :
      mensaje=message.text                              
      respuesta = ' '.join(mensaje.split(" ")[2:])   
      bot.send_message( -1001409931709, respuesta)
      bot.send_message(cid,"Mensaje enviado\n\n"+respuesta)
    
    
@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def command_bienvenida(m):
    cid = m.chat.id                                   
    cname = m.chat.title                              
    bienvenida = ""    
    nuevoUsuarioName = m.new_chat_member.username
    
        
    if nuevoUsuarioName == "Whatversionbot":
     
      if cid != -1001321250977:
        
        bot.send_message(cid, añadidoPor + " , para que hostias me metes, este no es mi grupo joderrr!")
        bot.leave_chat(cid)
        

    if (m.new_chat_member.username is None):          
        nun = m.new_chat_member.first_name            

        if (m.new_chat_member.last_name is not None): 
            nun += " "                        
            nun += m.new_chat_member.last_name
            n = nun         

        else:
          n = nun
    else:                                              
        nun = m.new_chat_member.username                                  
        n = " @"+nun

    bot.send_message(cid, str(saludos(n))+"  por favor lee las reglas usando el comando /reglas")

 
#bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))
bot.polling(none_stop=True)