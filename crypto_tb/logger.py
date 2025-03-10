import logging

logging.basicConfig(filename="trading_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

def log_trade(order_type, price, amount):
    logging.info(f"{order_type.upper()} order executed at {price} for {amount}")

def log_error(error_msg):
    logging.error(error_msg)
