

def validate_order(symbol, side, order_type, quantity, price):
    if not symbol:
        raise ValueError("Symbol is required")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("Valid price required for LIMIT order")