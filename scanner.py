from binance_client import get_futures_symbols, get_klines
from indicators import check_short_conditions, check_long_conditions
from telegram_bot import send_alert

def scan_all_markets():
    symbols = get_futures_symbols()
    for symbol in symbols:
        candles = get_klines(symbol)
        if candles:
            if check_short_conditions(candles):
                send_alert(symbol, "SHORT")
            elif check_long_conditions(candles):
                send_alert(symbol, "LONG")
