import sys
import pandas as pd

from src.config import *
from src.utils.logs import log_results
from src.utils.metrics import class_metrics
from src.utils.model_loader import load_model, load_scaler
from src.data.load_data import enhance_data# Function to load test data
from collections import Counter

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

def get_max_margin_distance(decision_scores_list: List[List[float]]) -> List[Tuple[int, float]]:
    # Define One-vs-One class pairs for 3 classes (0, 1, 2)
    class_pairs = [(0, 1), (0, 2), (1, 2)]  # 3 binary comparisons

    results = []

    for decision_scores in decision_scores_list:
        votes = []
        margin_dists = {}  # Store max margin distance per class

        # Iterate over the decision function values for this sample
        for i, (class1, class2) in enumerate(class_pairs):
            winner = class1 if decision_scores[i] > 0 else class2
            votes.append(winner)

            # Track max margin distance per class
            if winner not in margin_dists:
                margin_dists[winner] = abs(decision_scores[i])
            else:
                margin_dists[winner] = max(margin_dists[winner], abs(decision_scores[i]))

        # Get the final predicted class by majority vote
        predicted_class = Counter(votes).most_common(1)[0][0]

        # Get the highest margin distance for the predicted class
        max_margin_distance = margin_dists[predicted_class]

        results.append((predicted_class, max_margin_distance))

    return results


def lo_automaton(
    gamma: float,
    preds: List[int],
    margin_dists:  List[Tuple[int, float]],  # Nested list (each prediction has multiple class probabilities)
    prices: List[float]
) -> Tuple[int, int]:
    cash= CASH_INIT #initial cash value
    btc= BTC_INIT #initial btc value
    pv = PV_INIT #portfolio value at the beginning = initial cash investment
    min_return_ratio = sys.float_info.max

    step = 0.05  # Initial step size for gamma tuning
    prev_pv = pv  # Track previous portfolio value

    for i in range(len(prices)):
        if cash > 0: #if holding cash, buy btc
            # print(preds[i], margin_dists[i][0])
            if margin_dists[i][0]  == C2 and margin_dists[i][1] >= gamma:
                btc = cash / prices[i]
                pv = cash
                cash = 0
        else: # if holding btc, sell btc
            if margin_dists[i][0] == C0 and margin_dists[i][1] >= gamma: # signal to trade
                cash = btc * prices[i]
                btc = 0
                pv = cash

            return_ratio = (btc * prices[i] - pv) / pv # how much more percentage of value do we have (can be also negative)
            min_return_ratio = min(return_ratio, min_return_ratio)

            # gamma, step = optimize_gamma(gamma, step, prev_pv, pv)
            prev_pv = pv  # Update portfolio value for next iteration

            if return_ratio * 100 >= STOP_PROFIT or return_ratio * 100 <= STOP_LOSS: #if didnt get the signal => never allow to grab more profit or more loss than thresholds
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
    margin_dists = get_max_margin_distance(
        model.decision_function(X_transf).tolist()
    )
    class_index = list(model.classes_)  # Get correct class order
    c0_index = class_index.index(C0)  # Index of "Sell"
    c2_index = class_index.index(C2)

    accuracy, precision, recall, f1 = class_metrics(y_true, y_pred)
    prices = X["Close"].tolist()

    pv_highest = PV_INIT
    min_rr= sys.float_info.max

    gamma = GAMMA
    optimal_gamma = gamma

    pv, mrr = lo_automaton(gamma, y_pred, margin_dists, prices)

    if pv > pv_highest: # for optimal gamma, record the metrics
        optimal_gamma = gamma
        pv_highest = max(pv, pv_highest)
        min_rr = min(min_rr, mrr)

    log_results(pv_highest, min_rr, optimal_gamma, accuracy, precision, recall, f1)

    return




