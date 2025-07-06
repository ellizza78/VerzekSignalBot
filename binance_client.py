from binance.client import Client
import os

client = Client(api_key=os.getenv("BINANCE_API_KEY"), api_secret=os.getenv("BINANCE_SECRET_KEY"))

def get_futures_symbols():
    exchange_info = client.futures_exchange_info()
    return [s['symbol'] for s in exchange_info['symbols'] if s['contractType'] == 'PERPETUAL' and 'USDT' in s['symbol'] and '1000' not in s['symbol']]

def get_klines(symbol):
    try:
        data = client.futures_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1HOUR, limit=100)
        return [[float(i) for i in item[0:6]] for item in data]
    except Exception:
        return None
