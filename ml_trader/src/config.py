SVM_MODEL_PATH = "models/svm/svm_model.pkl"
SVM_SCALER_PATH = "models/svm/svm_scaler.pkl"


#fetch data
SYMBOL = "BTCUSDT"
TIME_STAMP1 = "2018-01-01"
TIME_STAMP2 ="2023-03-11"
TIME_STAMP3 ="2024-03-11"

#data
BTCUSDT_data_path = "data/BTCUSDT_hourly.csv"
BTCUSDT_backtest_data_path = "data/BTCUSDT_hourly_backtest.csv"

#long_only strat
GAMMA_THRESHOLD = 0.395  # gamma threshold to act on prediction, for we have three classes - uniform = 0.33 so something hi
CASH_INIT = 100  # initial cash value
BTC_INIT = 0  # initial btc value
PV_INIT = CASH_INIT  # portfolio value at the beginning = initial cash investment
STOP_PROFIT = 1000  # profit value to get out of the market
STOP_LOSS = 90  # loss value to get out of the market

