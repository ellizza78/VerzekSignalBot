from binance.client import Client
from binance.exceptions import BinanceAPIException
from config import BINANCE_API_KEY, BINANCE_SECRET_KEY, BINANCE_TESTNET
import time

def create_client():
    try:
        if BINANCE_TESTNET:
            client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY, testnet=True)
            client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        else:
            client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)
        # Simple ping to confirm connection
        client.ping()
        return client
    except BinanceAPIException as e:
        print("❌ Binance API Exception:", e.message)
        return None

def get_futures_symbols(client):
    try:
        exchange_info = client.futures_exchange_info()
        all_symbols = [s['symbol'] for s in exchange_info['symbols'] if s['contractType'] == 'PERPETUAL']
        # Optional: Filter out meme coins or specific symbols
        filtered = [s for s in all_symbols if not any(mem in s.lower() for mem in ['doge', 'pepe', 'floki', '1000', 'meme'])]
        return filtered
    except Exception as e:
        print("⚠️ Could not retrieve symbols:", str(e))
        return []

def get_klines(client, symbol, interval='15m', limit=100):
    try:
        return client.futures_klines(symbol=symbol, interval=interval, limit=limit)
    except Exception as e:
        print(f"⚠️ Could not get klines for {symbol}: {e}")
        return []
