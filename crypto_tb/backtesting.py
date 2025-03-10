import data_fetcher
import strategy

def backtest():
    df = data_fetcher.fetch_market_data()
    df = strategy.generate_signals(df)

    initial_balance = 1000
    balance = initial_balance
    position = 0
    for index, row in df.iterrows():
        if row["Position"] == 1:
            position = balance / row["close"]
            balance = 0
        elif row["Position"] == -1 and position > 0:
            balance = position * row["close"]
            position = 0

    print(f"Final Balance: {balance} (Initial: {initial_balance})")

backtest()
