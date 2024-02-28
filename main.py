from flask import Flask, jsonify, request
import os

app = Flask(__name__)
  
code = "nada"

@app.route('/')
def index():
    print(request.headers)
    print(request.json)
    #print(request)
    try:
      code = request.args.get("code", "nada")
    except:
      pass
    #return jsonify(success=True)
    #return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})
    return jsonify({"code": code})

@app.route("/asaas", methods=['POST'])
def wh():
    print(request.headers)
    print(request.json)
    #print(request)
    return jsonify(success=True)


#if __name__ == '__main__':
#    app.run(debug=True, port=os.getenv("PORT", default=5000))
