from flask import Flask, request, jsonify
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN")
AUTHORIZED_IP = "149.154."  # Telegram webhook IP range

latest_code = None

# Incoming Telegram Webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    global latest_code

    # Telegram safety
    if not request.remote_addr.startswith(AUTHORIZED_IP):
        return "Unauthorized", 403

    data = request.get_json()

    if "message" in data:
        text = data["message"].get("text", "")

        if text.startswith("code:"):
            code = text.replace("code:", "").strip()
            latest_code = code
            print("New Stake Code:", latest_code)

    return jsonify(status="ok"), 200


# API for browser extension to fetch last code
@app.route("/get-code", methods=["GET"])
def get_code():
    if latest_code:
        return jsonify({"code": latest_code})
    return jsonify({"code": None})


# Root
@app.route("/")
def home():
    return "Stake Claimer Server Running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
