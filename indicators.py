import ta
import pandas as pd

def check_short_conditions(candles):
    df = pd.DataFrame(candles)
    df.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    df = df.astype(float)

    df['ma7'] = df['close'].rolling(window=7).mean()
    df['ma25'] = df['close'].rolling(window=25).mean()
    df['ma95'] = df['close'].rolling(window=95).mean()
    rsi = ta.momentum.RSIIndicator(close=df['close'], window=14).rsi()
    stoch = ta.momentum.StochasticOscillator(df['high'], df['low'], df['close'], window=14, smooth_window=3)

    latest = df.iloc[-1]
    if latest['ma7'] < latest['ma25'] < latest['ma95']:
        if rsi.iloc[-1] < 70 and rsi.iloc[-2] > 70:
            if stoch.stoch().iloc[-1] < stoch.stoch_signal().iloc[-1] and stoch.stoch().iloc[-1] > 80:
                return True
    return False

def check_long_conditions(candles):
    df = pd.DataFrame(candles)
    df.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    df = df.astype(float)

    df['ma7'] = df['close'].rolling(window=7).mean()
    df['ma25'] = df['close'].rolling(window=25).mean()
    df['ma95'] = df['close'].rolling(window=95).mean()
    rsi = ta.momentum.RSIIndicator(close=df['close'], window=14).rsi()
    stoch = ta.momentum.StochasticOscillator(df['high'], df['low'], df['close'], window=14, smooth_window=3)

    latest = df.iloc[-1]
    if latest['ma7'] > latest['ma25'] > latest['ma95']:
        if 45 <= rsi.iloc[-1] <= 55 and rsi.iloc[-1] > rsi.iloc[-2]:
            if stoch.stoch().iloc[-2] < stoch.stoch_signal().iloc[-2] and stoch.stoch().iloc[-1] > stoch.stoch_signal().iloc[-1] and stoch.stoch().iloc[-1] < 20:
                return True
    return False
