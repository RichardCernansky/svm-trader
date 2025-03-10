import time
import data_fetcher
import strategy
import trade_executor

while True:
    try:
        df = data_fetcher.fetch_market_data()
        df = strategy.generate_signals(df)
        trade_executor.execute_trade(df)
        time.sleep(3600)  # Run every hour
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(60)  # Wait and retry
