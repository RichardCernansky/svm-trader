import pandas as pd
import numpy as np
import ta
from sklearn.model_selection import train_test_split


def load_crypto_data(filename):
    """
    Load and preprocess crypto data for model training/testing.

    Args:
        filename (str): Path to CSV file containing historical crypto data.
        test (bool): If True, return only test data. Otherwise, return train & test sets.

    Returns:
        If test=False: (X_train, X_test, y_train, y_test)
        If test=True: (X_test, y_test)
    """

    # Load dataset
    df = pd.read_csv(filename, parse_dates=["timestamp"])
    df.set_index("timestamp", inplace=True)

    # Compute log returns
    df["log_return"] = np.log(df["Close"] / df["Close"].shift(1)) / np.log(df["Close"])
    ret_std = df["log_return"].std()

    # Define labels based on 1-hour interval price movement
    df["label"] = 0  # Default class (no significant movement)
    df.loc[df["log_return"] >= ret_std, "label"] = 1  # Uptrend
    df.loc[df["log_return"] <= ret_std, "label"] = -1  # Downtrend

    # === Technical Indicators ===
    # Bollinger Bands
    df["bb_high"] = ta.volatility.bollinger_hband(df["Close"])  # SMA + 2σ
    df["bb_low"] = ta.volatility.bollinger_lband(df["Close"])  # SMA - 2σ
    df["bb_pct"] = (df["Close"] - df["bb_low"]) / (df["bb_high"] - df["bb_low"])  # Price position in bands

    # Moving Average Convergence Divergence (MACD)
    df["macd"] = ta.trend.macd(df["Close"])
    df["macd_signal"] = ta.trend.macd_signal(df["Close"])

    # Relative Strength Index (RSI)
    df["rsi"] = ta.momentum.rsi(df["Close"])

    # Remove NaN values caused by technical indicators
    df.dropna(inplace=True)

    return df


def data_train_test(filename, test=False):
    df = load_crypto_data(filename)

    # === Feature Selection ===
    features = ["Close", "Volume", "log_return", "bb_pct", "macd", "macd_signal", "rsi"]
    X = df[features]
    y = df["label"]

    # Split into training (80%) and testing (20%) sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    if test:
        return X_test, y_test

    return X_train, X_test, y_train, y_test

def data_backtest(filename):
    df = load_crypto_data(filename)
    features = ["Close", "Volume", "log_return", "bb_pct", "macd", "macd_signal", "rsi"]
    X = df[features]

    return X