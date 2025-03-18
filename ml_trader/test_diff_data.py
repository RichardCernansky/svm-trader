
from src.config import *
from src.data.fetch_data import get_binance_ohlcv
from src.models.model_trainer import train_model
from src.strategies.long_only_testing import run_lo_automaton
from src.utils.logs import process_log

def test_diff_data():

    # 1. fetch data
    # for each data
        # 2. train model
        # 3. lo_automaton test
        # 4. log_results
    # plot results

    train_periods = [] # periods[i] = ["start_date", "end_date"]
    test_periods = []

    for i in range(len(train_periods)):
        train_data = get_binance_ohlcv(train_periods[i][0], train_periods[i][1])
        test_data = get_binance_ohlcv(test_periods[i][0], test_periods[i][1])

        trained_model_path, train_scaler_path = train_model(MODEL, train_data)
        run_lo_automaton(trained_model_path, train_scaler_path, test_data)

        processed_log = process_log()
        # plot the processed_log

    return
