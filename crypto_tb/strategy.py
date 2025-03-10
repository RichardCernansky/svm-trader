import numpy as np
import indicators

def generate_signals(df):
    df = indicators.compute_sma(df)
    df["Signal"] = np.where(df["SMA_Short"] > df["SMA_Long"], 1, 0)
    df["Position"] = df["Signal"].diff()
    return df
