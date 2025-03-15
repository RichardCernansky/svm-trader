import pandas as pd
import requests
import time
import src.config

from src.config import *

def get_binance_ohlcv(start, end, symbol="BTCUSDT", interval="1h"):
    """fetches from Binance API into local machine"""

    base_url = "https://api.binance.com/api/v3/klines"
    df_list = []

    start_ts = int(pd.Timestamp(start).timestamp() * 1000)
    end_ts = int(pd.Timestamp(end).timestamp() * 1000)

    while start_ts < end_ts:
        url = f"{base_url}?symbol={symbol}&interval={interval}&startTime={start_ts}&limit=1000"
        response = requests.get(url).json()

        if not response:
            break  # No more data available

        df = pd.DataFrame(response, columns=[
            "timestamp", "Open", "High", "Low", "Close", "Volume",
            "Close_time", "Quote_asset_volume", "Number_of_trades",
            "Taker_buy_base_vol", "Taker_buy_quote_vol", "Ignore"
        ])

        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")  # Convert to datetime
        df.set_index("timestamp", inplace=True)
        df = df[["Open", "High", "Low", "Close", "Volume"]].astype(float)
        df_list.append(df)

        start_ts = int(df.index[-1].timestamp() * 1000) + 1  # Move to next batch
        time.sleep(0.5)  # Prevent API rate limits

    return pd.concat(df_list)

print("Started fetching...")

btc_data = get_binance_ohlcv(TIME_STAMP2, TIME_STAMP3, SYMBOL, "1h",)
data = btc_data.to_csv("data/BTCUSDT_hourly_backtest.csv")

if data is not None: print("Successfully saved data.")
else: print("Failed to save data.")


print(btc_data.head())