STOP_LOSS_PERCENT = 0.02  # 2% stop-loss
TAKE_PROFIT_PERCENT = 0.05  # 5% take-profit

def calculate_stop_loss(entry_price):
    return entry_price * (1 - STOP_LOSS_PERCENT)

def calculate_take_profit(entry_price):
    return entry_price * (1 + TAKE_PROFIT_PERCENT)
