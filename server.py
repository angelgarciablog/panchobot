from flask import Flask
from bot import bot
app = Flask(__name__)

WEBHOOK_URL_PATH = "/{}".format(bot.token)

# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


if __name__ == "__main__":
  
  app.run()
