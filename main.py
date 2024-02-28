from flask import Flask, jsonify, request
import os
import telebot

bot_aux = os.getenv("BOT_AUX_TOKEN")
bot = telebot.TeleBot(bot_aux)

app = Flask(__name__)

code = "nada"

@app.route('/')
def index():
    global code
    print(request.headers)
    print(request.json)
    #print(request)
    try:
      code = request.args.get("code", "nada")
    except:
      pass
    #return jsonify(success=True)
    #return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})
    bot.send_message("556068392", code)
    return jsonify({"code": code})

@app.route("/asaas", methods=['POST'])
def wh():
    print(request.headers)
    print(request.json)
    #print(request)
    return jsonify(success=True)


#if __name__ == '__main__':
#    app.run(debug=True, port=os.getenv("PORT", default=5000))

app.run(host='0.0.0.0', port=8080)
