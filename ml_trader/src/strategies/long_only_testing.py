import sys


from src.config import *
from src.utils.metrics import class_metrics
from src.utils.model_loader import load_model, load_scaler
from src.data.load_data import data_train_test, data_backtest  # Function to load test data

#set up model
MODEL_PATH = SVM_MODEL_PATH
SCALER_PATH = SVM_SCALER_PATH


def long_only_automaton(gamma, preds, margin_dists, prices) -> [int, int]:
    cash= CASH_INIT #initial cash value
    btc= BTC_INIT #initial btc value
    pv = PV_INIT #portfolio value at the beginning = initial cash investment
    min_return_ratio = sys.float_info.max

    c1 = 1
    c2 = -1
    c3 = 0 # for clarity we also have the 3rd neutral class

    for i in range(len(prices)):
        if cash > 0:
            if preds[i] == c1 and margin_dists[i] >= gamma:
                btc = cash / prices[i]
                pv = cash
                cash = 0
        else:
            if preds[i] == c2 and margin_dists[i] >= gamma:
                cash = btc * prices[i]
                btc = 0
                pv = cash

            return_ratio = (btc * prices[i] - pv) / pv
            min_return_ratio = min(min_return_ratio, return_ratio)

            if return_ratio >= STOP_PROFIT or return_ratio <= STOP_LOSS:
                cash = btc * prices[i]
                btc = 0
                pv = cash

    return pv, min_return_ratio



# Load test data (Ensure dataset has already been preprocessed)
df, y_true = data_backtest(BTCUSDT_backtest_data_path)  # Example function
print(df.head())

# Load trained model & scaler
model = load_model(MODEL_PATH)
scaler = load_scaler(SCALER_PATH)

# Scale test data
df_transf = scaler.transform(df)

# Make predictions and prep for long_only
y_pred = model.predict(df_transf).tolist()
y_pred_probs = model.predict_proba(df_transf).tolist()
accuracy, precision, recall, f1 = class_metrics(y_true, y_pred)
prices = df["Close"].tolist()

pv_highest = 0
min_rr= sys.float_info.max
optimal_gamma = GAMMAS[0]
for gamma in GAMMAS:
    margin_dist = [prob[y_pred[i]] - gamma for i,prob in enumerate(y_pred_probs)]
    pv, mrr = long_only_automaton(gamma, y_pred, margin_dist, prices)

    if pv > pv_highest: # for obtaining the optimal gamma
        optimal_gamma = gamma
        pv_highest = max(pv, pv_highest)
    min_return_ratio = min(min_rr, mrr)


#log values
# MODEL_PATH
# pv_highest
# pv_ratio
# min_return_ratio - for risk assessment
# optimal_gamma
perc_ret = round((pv_highest/PV_INIT - 1) * 100,4)
with open(LOGFILE, "a") as f:
    f.write(f"MODEL_PATH = {MODEL_PATH}\n")
    f.write(f"pv_highest = {pv_highest}\n")
    f.write(f"perc_ret = {perc_ret}%\n")
    f.write(f"min_return_ratio = {min_rr}  # For risk assessment\n")
    f.write(f"optimal_gamma = {optimal_gamma}\n")
    f.write(f"A, P, R, F1 = {accuracy, precision, recall, f1}\n")



print(f"Highest Portfolio value: {pv_highest}: Percentage return: {perc_ret}%")






