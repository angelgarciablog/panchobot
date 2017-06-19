import telebot
from os import environ

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN'])
# print(bot.token)
# Iniciar la variable del contador
contador = 0
bot_text = '''
Howdy, how are you doing?
haz clic en /contar
Source code on https://glitch.com/~{}
'''.format(environ['PROJECT_NAME'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, bot_text)

  
@bot.message_handler(commands=['contar'])
def send_contador(message):
  # Traer la variable global para editarla.
  global contador
  # Incrementar
  contador += 1
  # Listo (?)
  bot.reply_to(message, 'Cuenta actual: {}'.format(contador))

bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))