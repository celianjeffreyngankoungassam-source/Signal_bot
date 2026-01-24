from flask import Flask, request
import requests

# =========================
# CONFIGURATION
# =========================

app = Flask(__name__)

BOT_TOKEN = 8392781220:AAG6KzoEZe_EyBLU4m5uft8DJnmKU8w_JGo      
CHAT_ID = 6048358843         

TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

# =========================
# ROUTE WEBHOOK TELEGRAM
# =========================

@app.route("/webhook", methods=["POST"])
def telegram_webhook():
    data = request.get_json()

    if not data:
        return "no data", 400

    message = data.get("message")
    if not message:
        return "ok", 200

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    # Réponse automatique
    requests.post(
        f"{TELEGRAM_API}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": f"Reçu ✅ : {text}"
        }
    )

    return "ok", 200

# =========================
# ROUTE TEST (OPTIONNELLE)
# =========================

@app.route("/")
def index():
    return "Bot Telegram Flask OK ✅"

# =========================
# LANCEMENT DU SERVEUR
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)