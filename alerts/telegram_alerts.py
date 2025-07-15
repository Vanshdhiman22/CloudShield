import requests

# 🔐 Replace these with your real values
BOT_TOKEN = '7982386040:AAHw1J0zTxj8qCC4rGOc_EAbUdXAUVCAe_Y'
CHAT_ID = '1443429338'

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"Telegram Error: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print("Exception in sending Telegram alert:", e)
        return False
