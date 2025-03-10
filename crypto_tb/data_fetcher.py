import pandas as pd
import exchange
import config

def fetch_market_data(symbol=config.TRADE_SYMBOL, timeframe=config.TIMEFRAME, limit=200):
    bars = exchange.exchange.fetch_ohlcv(symbol, timeframe, limit)
    df = pd.DataFrame(bars, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df
