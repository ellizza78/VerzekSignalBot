import requests
import os

def send_alert(symbol, signal_type):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    emoji = "🚀" if signal_type == "LONG" else "🔻"
    message = f"""
{emoji} {signal_type} SIGNAL DETECTED!
Symbol: {symbol}
Conditions matched!
— Verzek Signal Bot
"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message.strip()}
    requests.post(url, data=data)
