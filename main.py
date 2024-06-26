from flask import Flask, jsonify, request
import os
import telebot
import requests

bot_aux = os.getenv("BOT_AUX_TOKEN")
bot = telebot.TeleBot(bot_aux)

app = Flask(__name__)

code = "nada"
state = "nenhum"

@app.route('/')
def index():
    global code
    global state
    #print(request.headers)
    #print(request.json)
    #print(request)
    try:
      code = request.args.get("code", code)
    except:
      pass
    try:
      state = request.args.get("state", state)
    except:
      pass
    #return jsonify(success=True)
    #return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})
    bot.send_message("556068392", "code: " + code + "\nstate: " + state)
    return jsonify({"code": code, "state": state})

@app.route("/asaas", methods=['POST'])
def wh():
    print(request.headers)
    print(request.json)
    #print(request)
    return jsonify(success=True)

notificacoes = []
headers = []

@app.route("/", methods=['POST'])
def ml():
    global notificacoes
    global headers
    print(request.headers)
    print(request.json)
    notificacoes.append(request.json)
    headers.append(request.headers)
    #print(request)
    repassar(request.json)
    return jsonify(success=True)

def repassar(dados):
    requests.post("http://200.195.166.130:8080/ReceptorWebhooks/mercadolivre/webhooks/receiver", json=dados)

@app.route("/nt", methods=['POST'])
def nt():
    global notificacoes
    global headers
    print(request.headers)
    print(request.json)
    notificacoes.append(request.json)
    headers.append(request.headers)
    #print(request)
    repassar(request.json)
    return jsonify(success=True)
    
@app.route("/vn", methods=['GET'])
def vn():
    global notificacoes
    global headers
    #return jsonify(notificacoes=notificacoes, headers=str(headers))
    return jsonify(notificacoes=notificacoes)

#if __name__ == '__main__':
#    app.run(debug=True, port=os.getenv("PORT", default=5000))

app.run(host='0.0.0.0', port=8080)
