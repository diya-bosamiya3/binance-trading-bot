# #!/usr/bin/env python3
# """
# Trading Bot CLI — Binance Futures Testnet
# Usage examples:
#   python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01
#   python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 70000
# """

# import argparse
# import os
# import sys

# from dotenv import load_dotenv

# from bot.client import BinanceClient, BinanceClientError
# from bot.logging_config import setup_logger
# from bot.orders import place_order
# from bot.validators import ValidationError, validate_inputs

# load_dotenv()
# logger = setup_logger()


# def get_credentials():
#     """Read API credentials from environment variables."""
#     api_key = os.getenv("BINANCE_API_KEY", "").strip()
#     api_secret = os.getenv("BINANCE_API_SECRET", "").strip()

#     if not api_key or not api_secret:
#         print("\n❌ Missing API credentials.")
#         print("   Create a .env file with:")
#         print("   BINANCE_API_KEY=your_key_here")
#         print("   BINANCE_API_SECRET=your_secret_here\n")
#         logger.error("API credentials not found in environment.")
#         sys.exit(1)

#     return api_key, api_secret


# def parse_args():
#     parser = argparse.ArgumentParser(
#         description="Place orders on Binance Futures Testnet",
#         formatter_class=argparse.RawDescriptionHelpFormatter,
#         epilog="""
# Examples:
#   Market buy:
#     python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01

#   Limit sell:
#     python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 70000
#         """
#     )
#     parser.add_argument("--symbol",  required=True,  help="Trading pair, e.g. BTCUSDT")
#     parser.add_argument("--side",    required=True,  help="BUY or SELL")
#     parser.add_argument("--type",    required=True,  dest="order_type", help="MARKET or LIMIT")
#     parser.add_argument("--qty",     required=True,  type=float, help="Order quantity")
#     parser.add_argument("--price",   required=False, type=float, default=None,
#                         help="Limit price (required for LIMIT orders)")
#     return parser.parse_args()


# def main():
#     args = parse_args()

#     logger.info("="*40)
#     logger.info("Trading bot started")
#     logger.info(f"Input: symbol={args.symbol} side={args.side} "
#                 f"type={args.order_type} qty={args.qty} price={args.price}")

#     # Step 1: Validate inputs
#     try:
#         validated = validate_inputs(
#             symbol=args.symbol,
#             side=args.side,
#             order_type=args.order_type,
#             quantity=args.qty,
#             price=args.price,
#         )
#     except ValidationError as e:
#         print(f"\n❌ Invalid input:\n{e}\n")
#         sys.exit(1)

#     # Step 2: Load credentials and create client
#     api_key, api_secret = get_credentials()
#     client = BinanceClient(api_key, api_secret)

#     # Step 3: Place the order
#     try:
#         place_order(
#             client=client,
#             symbol=validated["symbol"],
#             side=validated["side"],
#             order_type=validated["order_type"],
#             quantity=validated["quantity"],
#             price=validated["price"],
#         )
#     except (BinanceClientError, ValueError) as e:
#         logger.error(f"Order failed: {e}")
#         sys.exit(1)

#     logger.info("Trading bot finished successfully")


# if __name__ == "__main__":
#     main()


import click
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

setup_logger()

@click.command()
@click.option('--symbol', required=True, help='Trading symbol (e.g., BTCUSDT)')
@click.option('--side', required=True, help='BUY or SELL')
@click.option('--type', 'order_type', required=True, help='MARKET or LIMIT')
@click.option('--quantity', required=True, type=float)
@click.option('--price', required=False, type=float)
def trade(symbol, side, order_type, quantity, price):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        print("\n📌 Order Summary:")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")

        if order_type == "MARKET":
            res = place_market_order(symbol, side, quantity)
        else:
            res = place_limit_order(symbol, side, quantity, price)

        print("\n✅ Order Successful!")
        print(f"Order ID: {res['orderId']}")
        print(f"Status: {res['status']}")
        print(f"Executed Qty: {res['executedQty']}")
        print(f"Avg Price: {res['avgPrice']}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    trade()
