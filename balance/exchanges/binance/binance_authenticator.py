from binance import Client

def get_balance(api_key, api_secret):
    client = Client(api_key, api_secret)
    balance = client.get_asset_balance(asset='BTC')