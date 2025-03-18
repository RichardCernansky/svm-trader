from src.config import *

def log_results(pv_highest, min_return_ratio, optimal_gamma, accuracy, precision, recall, f1):
    # log values
    # MODEL_PATH
    # pv_highest
    # pv_ratio
    # min_return_ratio - for risk assessment
    # optimal_gamma
    perc_ret = round((pv_highest / PV_INIT - 1) * 100, 4)
    min_return_ratio = round(min_return_ratio * 100, 8)
    optimal_gamma = round(optimal_gamma, 8)
    with open(LOGFILE, "a") as f:
        f.write(f"model = {MODEL}\n")
        f.write(f"pv_highest = {pv_highest}\n")
        f.write(f"perc_ret = {perc_ret}%\n")
        f.write(f"min_return_ratio = {min_return_ratio}%\n")  # For risk assessment
        f.write(f"optimal_gamma = {optimal_gamma}\n")
        f.write(f"A, P, R, F1 = {accuracy, precision, recall, f1}\n")
        f.write(f"\n")

    print(f"Highest Portfolio value: {pv_highest}: Percentage return: {perc_ret}%")

def process_log():

    return