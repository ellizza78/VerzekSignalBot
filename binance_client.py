from binance.client import Client
import os

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

# ✅ Connect to Binance Futures Testnet (SAFE for restricted regions)
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
