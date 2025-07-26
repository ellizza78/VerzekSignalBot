import requests
import time

# === CoinRanking API Key Rotation ===
COINRANKING_KEYS = [
    "coinranking265c40af7de0f7e6e34ed4d23d853be80f7637bdda0edd28 -1",
    "coinranking8352ab1e49611aa3fdd91060ef6b5b82403970be2446da63 -2",
    "coinranking57ff76f91a256a110c5e9e2cf523a52e9803cfb406e878a4 -3",
    "coinranking6d76eeaa95660c9fd1b485042b2912aa4d4035e1482a7f66 -4"
]
key_index = 0
last_used_key_time = 0

def get_next_coinranking_key():
    global key_index, last_used_key_time
    key_index = (key_index + 1) % len(COINRANKING_KEYS)
    last_used_key_time = time.time()
    return COINRANKING_KEYS[key_index]

# === Binance Futures Price ===
def get_price_from_binance(symbol):
    try:
        url = f"https://fapi.binance.com/fapi/v1/ticker/price?symbol={symbol}USDT"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return float(r.json()["price"]), "Binance Futures"
    except Exception:
        pass
    return None, None

# === CoinRanking Price ===
def get_price_from_coinranking(uuid):
    global key_index
    try:
        key = COINRANKING_KEYS[key_index]
        url = f"https://api.coinranking.com/v2/coin/{uuid}"
        headers = {"x-access-token": key}
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            data = r.json()
            price = float(data["data"]["coin"]["price"])
            return price, f"CoinRanking (Key {key_index + 1})"
        elif r.status_code in [401, 429]:
            key = get_next_coinranking_key()
            headers = {"x-access-token": key}
            r = requests.get(url, headers=headers, timeout=5)
            if r.status_code == 200:
                data = r.json()
                price = float(data["data"]["coin"]["price"])
                return price, f"CoinRanking (Key {key_index + 1})"
    except Exception:
        pass
    return None, None

# === CoinGecko Price ===
def get_price_from_coingecko(symbol):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return float(data[symbol.lower()]["usd"]), "CoinGecko"
    except Exception:
        pass
    return None, None

# === Main Price Fallback Function ===
def get_price(symbol, uuid=None):
    sources = [
        lambda: get_price_from_binance(symbol),
        lambda: get_price_from_coinranking(uuid) if uuid else (None, None),
        lambda: get_price_from_coingecko(symbol)
    ]

    for source in sources:
        price, provider = source()
        if price:
            print(f"[INFO] Price for {symbol} fetched from {provider}: ${price}")
            return price

    print(f"[ERROR] Failed to fetch price for {symbol} from all sources.")
    return None
