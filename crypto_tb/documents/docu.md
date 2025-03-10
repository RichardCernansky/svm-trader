## Suggested module structure

```bash
crypto_trading_bot/
│── main.py              # Main script to run the bot
│── config.py            # Configuration settings (API keys, trading pairs, etc.)
│── exchange.py          # Handles connection to exchange (Binance)
│── data_fetcher.py      # Fetches historical and real-time price data
│── indicators.py        # Implements technical indicators (SMA, EMA, MACD, RSI, etc.)
│── strategy.py          # Defines the trend-following strategy logic
│── trade_executor.py    # Handles order placement and execution
│── risk_management.py   # Implements stop-loss, take-profit, position sizing
│── backtesting.py       # Simulates strategy performance on historical data
│── logger.py            # Logs trade history, errors, and analytics
│── utils.py             # Helper functions (date conversion, error handling, etc.)
│── requirements.txt     # Dependencies (pip install -r requirements.txt)
│── README.md            # Documentation on how to use the bot

#generate diagram
pyreverse -o png  .
#find word in subtree files
find . -type f -print | xargs grep "backtesting"
```
