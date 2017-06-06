import flask, telebot
from bot import bot

app = flask.Flask(__name__, static_url_path='')

WEBHOOK_URL_PATH = "/{}".format(bot.token)


# Process index page
@app.route('/')
def root():
    print('index!')
    return app.send_static_file('index.html')


@app.route('/style.css')
def style():
  return app.send_static_fie('style.css')


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
