from flask import Flask
import telebot
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/giuliano")
def giuliano():
  return "Ciao Giuliano!"

if __name__ == "__main__":
  
  app.run()
