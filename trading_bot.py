from alpaca_trade_api import REST


# Replace with your API keys
API_KEY = 'PK5YABLLYMDH4UWQ28BV'
SECRET_KEY = '2kdR5Fsrkf1pPru0xhHb1zcoCDaVtGhiRiS8KVAd'
BASE_URL = 'https://paper-api.alpaca.markets' # Paper trading environment

# Create a trading client instance for paper trading
trading_client = REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

# Get the list of orders
try:
    orders = trading_client.list_orders(status='all')  # 'all' will fetch filled, pending, and canceled orders
    
    if len(orders) > 0:
        for order in orders:
            print(f"Order {order.id}: {order.symbol} {order.qty} shares - Status: {order.status}")
    else:
        print("No orders found.")

except Exception as e:
    print(f"An error occurred: {e}")