from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Bot Flask actif sur Render"

@app.route("/test")
def test():
    return jsonify({
        "status": "ok",
        "message": "Endpoint /test fonctionne"
    })

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Données reçues :", data)
    return jsonify({"received": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
import requests
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))