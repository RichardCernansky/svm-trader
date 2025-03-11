import pandas as pd
import numpy as np
import ta

def load_data(filename):

    df = pd.read_csv(filename, parse_dates=["timestamp"])
    df.set_index("timestamp", inplace=True)

    df["log_return"] = (df["Close"] / df["Close"].shift(1)).apply(lambda x: np.log(x))
    df.dropna(inplace=True)

    #define labels based on 1-hour interval prive movement
    df["label"] = 0
    df.loc[df["log_return"] >= 0.005, "label"] = 1
    df.loc[df["log_return"] <= -0.005, "label"] = -1


    #technical indicators
    # Bollinger Bands
    df["bb_high"] = ta.volatility.bollinger_hband(df["Close"]) # sma + 2sigma
    df["bb_low"] = ta.volatility.bollinger_lband(df["Close"]) # sma - 2sigma
    df["bb_pct"] = (df["Close"] - df["bb_low"]) / (df["bb_high"] - df["bb_low"]) # portion of the space between bb_high and bb_low

    # Moving Average Convergence Divergence (MACD)
    df["macd"] = ta.trend.macd(df["Close"])
    df["macd_signal"] = ta.trend.macd_signal(df["Close"])

    # Relative Strength Index (RSI)
    df["rsi"] = ta.momentum.rsi(df["Close"])

    # Remove NaN values from newly created indicators
    df.dropna(inplace=True)

    return df