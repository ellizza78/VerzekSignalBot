import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Binance API credentials
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

# Toggle this to True if you're using Testnet
BINANCE_TESTNET = os.getenv("BINANCE_TESTNET", "False").lower() == "true"

# Telegram credentials
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
