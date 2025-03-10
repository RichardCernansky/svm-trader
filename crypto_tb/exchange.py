import ccxt
import config

def connect_to_exchange():
    return ccxt.binance({
        "apiKey": config.API_KEY,
        "secret": config.API_SECRET,
        "options": {"adjustForTimeDifference": True}
    })

exchange = connect_to_exchange()

def get_balance():
    return exchange.fetch_balance()

def place_order(order_type, symbol=config.TRADE_SYMBOL, amount=config.TRADE_AMOUNT):
    try:
        if order_type == "buy":
            return exchange.create_market_buy_order(symbol, amount)
        elif order_type == "sell":
            return exchange.create_market_sell_order(symbol, amount)
    except Exception as e:
        print(f"Order failed: {e}")
        return None
