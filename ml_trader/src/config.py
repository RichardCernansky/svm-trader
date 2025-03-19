#CONFIGS

#fetch data
SYMBOL = "BTCUSDT"
INTERVAL = "1h"

START_DATE = "2017-01-01"
END_DATE = "2025-03-11"
TRAIN_MONTHS =24
TEST_MONTHS = 12

LOGFILE = "data/logs/log.txt"
MODEL = "svm"

#data
BTCUSDT_data_path = "data/BTCUSDT_hourly.csv"
BTCUSDT_backtest_data_path = "data/BTCUSDT_hourly_backtest.csv"

#long_only strat
CASH_INIT = 100  # initial cash value
BTC_INIT = 0  # initial btc value
PV_INIT = CASH_INIT  # portfolio value at the beginning = initial cash investment
STOP_PROFIT = 50  # (%) profit value to get out of the market  | adjusts behavior, higher stop => waits for larger profit, but more risky
STOP_LOSS = -10  # (%) loss value to get out of the market,

DATA_FEATURES = ["Close", "Volume", "bb_pct", "macd", "macd_signal", "rsi"]
# GAMMAS = [0.34 + i * 0.0005 for i in range(200)]
# GAMMAS = [0.35]
GAMMA = 0.33 # | adjusts behavior, higher gamma => more conservative

C0 = -1
C1 = 0  # for clarity we also have the 3rd neutral class
C2 = 1




