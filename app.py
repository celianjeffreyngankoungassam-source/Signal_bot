import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{8392781220:AAG6KzoEZe_EyBLU4m5uft8DJnmKU8w_JGo}"

@app.route("/")
def home():
    return "🤖 Telegram Bot connecté à Flask"

@app.route("/test")
def test():
    return jsonify({"status": "ok"})

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if text == "/start":
        send_message(chat_id, "👋 Bienvenue sur Signal Forex IA")
    elif text.lower() == "test":
        send_message(chat_id, "✅ Bot opérationnel")
    else:
        send_message(chat_id, "📡 Signal reçu, analyse en cours...")

    return jsonify({"ok": True})

def send_message(chat_id, text):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)