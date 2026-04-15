
import logging
import random
import time

def generate_mock_response(symbol, side, order_type, quantity, price=None):
    order_id = random.randint(100000, 999999)
    status = "FILLED" if order_type == "MARKET" else "NEW"

    avg_price = price if price else round(random.uniform(50000, 70000), 2)

    response = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "orderId": order_id,
        "status": status,
        "executedQty": quantity if order_type == "MARKET" else 0,
        "avgPrice": avg_price
    }

    return response


def place_market_order(symbol, side, quantity):
    try:
        logging.info(f"Placing MOCK MARKET order: {symbol} {side} {quantity}")
        time.sleep(1)

        response = generate_mock_response(symbol, side, "MARKET", quantity)

        logging.info(f"Market Order Response: {response}")
        return response

    except Exception as e:
        logging.error(f"Market Order Error: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logging.info(f"Placing MOCK LIMIT order: {symbol} {side} {quantity} @ {price}")
        time.sleep(1)

        response = generate_mock_response(symbol, side, "LIMIT", quantity, price)

        logging.info(f"Limit Order Response: {response}")
        return response

    except Exception as e:
        logging.error(f"Limit Order Error: {str(e)}")
        raise