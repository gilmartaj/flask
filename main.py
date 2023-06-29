from flask import Flask, jsonify, request
import os

app = Flask(__name__)
  

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route("/asaas", methods=['POST'])
def wh():
    print(request.headers)
    print(request.json)
    #print(request)
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
