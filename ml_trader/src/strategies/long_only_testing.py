from src.config import *
from src.utils.model_loader import load_model, load_scaler
from src.data.load_data import data_train_test, data_backtest  # Function to load test data

#set up model
MODEL_PATH = SVM_MODEL_PATH
SCALER_PATH = SVM_SCALER_PATH


def long_only_automaton(preds, margin_dists, prices):
    cash= CASH_INIT #initial cash value
    btc= BTC_INIT #initial btc value
    pv = PV_INIT #portfolio value at the beginning = initial cash investment

    c1 = 1
    c2 = -1
    c3 = 0 # for clarity we also have the 3rd neutral class

    for i in range(len(prices)):
        if cash > 0:
            if preds[i] == c1 and margin_dists[i] >= GAMMA_THRESHOLD:
                btc = cash / prices[i]
                pv = cash
                cash = 0
        else:
            if preds[i] == c2 and margin_dists[i] >= GAMMA_THRESHOLD:
                cash = btc * prices[i]
                btc = 0
                pv = cash

            return_ratio = (btc * prices[i] - pv) / pv
            if return_ratio >= STOP_PROFIT or return_ratio <= STOP_LOSS:
                cash = btc * prices[i]
                btc = 0
                pv = cash

    return cash, btc, pv



# Load test data (Ensure dataset has already been preprocessed)
df = data_backtest(BTCUSDT_backtest_data_path)  # Example function
print(df.head())

# Load trained model & scaler
model = load_model(MODEL_PATH)
scaler = load_scaler(SCALER_PATH)

# Scale test data
df_transf = scaler.transform(df)

# Make predictions and prep for long_only
y_pred = model.predict(df_transf).tolist()
y_pred_probs = model.predict_proba(df_transf).tolist()
print(len(y_pred_probs))
prices = df["Close"].tolist()
margin_dist = [prob[y_pred[i]] - GAMMA_THRESHOLD for i,prob in enumerate(y_pred_probs)]

cash, btc, pv = long_only_automaton(y_pred, margin_dist, prices)

print(f"Cash: {cash}: Profit ratio: {cash/CASH_INIT}")
print(f"Remaining BTC: {btc}")
print(f"Portfolio value: {pv}: Profit ratio: {pv/PV_INIT}")






