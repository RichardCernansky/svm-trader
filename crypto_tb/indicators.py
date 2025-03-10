import pandas as pd
import config

def compute_sma(df, short=config.SMA_SHORT, long=config.SMA_LONG):
    df["SMA_Short"] = df["close"].rolling(window=short).mean()
    df["SMA_Long"] = df["close"].rolling(window=long).mean()
    return df
