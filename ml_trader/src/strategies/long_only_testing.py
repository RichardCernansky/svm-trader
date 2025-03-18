import sys
import pandas as pd

from src.config import *
from src.utils.logs import log_results
from src.utils.metrics import class_metrics
from src.utils.model_loader import load_model, load_scaler
from src.data.load_data import enhance_data# Function to load test data

from typing import List, Tuple

def optimize_gamma(
    gamma: float,
    step: float,
    prev_pv: float,
    new_pv: float,
) -> [float, float]:
    if new_pv > prev_pv:
        # If profit increased, continue adjusting gamma in the same direction
        gamma += step
    else:
        # If profit decreased, reverse the direction of adjustment and reduce step size
        gamma -= step
        step *= 0.5  # Reduce step size for finer adjustments

    # ensure gamma stays within valid range
    gamma = max(0.03, min(gamma, 1.0))

    return gamma, step



def lo_automaton(gamma, preds, margin_dists, prices) -> [int, int]:
    cash= CASH_INIT #initial cash value
    btc= BTC_INIT #initial btc value
    pv = PV_INIT #portfolio value at the beginning = initial cash investment
    min_return_ratio = 1000

    c1 = 1
    c2 = -1
    c3 = 0 # for clarity we also have the 3rd neutral class

    step = 0.05  # Initial step size for gamma tuning
    prev_pv = pv  # Track previous portfolio value

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

            return_ratio = (btc * prices[i] - pv) / pv # how much more percentage of value do we have (can be also negative)
            min_return_ratio = min(return_ratio, min_return_ratio)

            gamma, step = optimize_gamma(gamma, step, prev_pv, pv)
            prev_pv = pv  # Update portfolio value for next iteration

            if return_ratio >= STOP_PROFIT or return_ratio <= STOP_LOSS:
                cash = btc * prices[i]
                btc = 0
                pv = cash


    return pv, min_return_ratio

def run_lo_automaton(model_path: str, scaler_path: str, test_data: pd.DataFrame):
    # Load test data (Ensure dataset has already been preprocessed)
    test_data = enhance_data(test_data)
    X = test_data[DATA_FEATURES]
    y_true = test_data["label"]

    print(X.head())

    # Load trained model & scaler
    model = load_model(model_path)
    scaler = load_scaler(scaler_path)
    X_transf = scaler.transform(X)

    # Make predictions and prep for long_only
    y_pred = model.predict(X_transf).tolist()
    y_pred_probs = model.predict_proba(X_transf).tolist()
    accuracy, precision, recall, f1 = class_metrics(y_true, y_pred)
    prices = X["Close"].tolist()

    pv_highest = 0
    min_rr= sys.float_info.max
    optimal_gamma = GAMMAS[0]
    for gamma in GAMMAS:
        margin_dist = [prob[y_pred[i]] - gamma for i,prob in enumerate(y_pred_probs)]
        pv, mrr = lo_automaton(gamma, y_pred, margin_dist, prices)

        if pv > pv_highest: # for optimal gamma, record the metrics
            optimal_gamma = gamma
            pv_highest = max(pv, pv_highest)
            min_rr = min(min_rr, mrr)

    log_results(pv_highest, min_rr, optimal_gamma, accuracy, precision, recall, f1)

    return




