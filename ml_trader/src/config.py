SVM_MODEL_PATH = "models/svm/svm_model.pkl"
SVM_SCALER_PATH = "models/svm/svm_scaler.pkl"


#fetch data
SYMBOL = "BTCUSDT"
TIME_STAMP1 = "2020-01-01"
TIME_STAMP2 ="2024-03-11"
TIME_STAMP3 ="2025-03-11"

#data
BTCUSDT_data_path = "data/BTCUSDT_hourly.csv"
BTCUSDT_backtest_data_path = "data/BTCUSDT_hourly_backtest.csv"

#long_only strat
CASH_INIT = 100  # initial cash value
BTC_INIT = 0  # initial btc value
PV_INIT = CASH_INIT  # portfolio value at the beginning = initial cash investment
STOP_PROFIT = 1000  # profit value to get out of the market
STOP_LOSS = 90  # loss value to get out of the market


features = ["Close", "Volume", "bb_pct", "macd", "macd_signal", "rsi"]
GAMMAS = [0.34 + i * 0.0005 for i in range(200)]


#Temp logfile
LOGFILE = "data/logs/log.txt"