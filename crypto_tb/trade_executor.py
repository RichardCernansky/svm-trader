import exchange

def execute_trade(df):
    last_position = df["Position"].iloc[-1]

    if last_position == 1:
        print("BUY Signal detected! Placing order...")
        exchange.place_order("buy")
    elif last_position == -1:
        print("SELL Signal detected! Placing order...")
        exchange.place_order("sell")
