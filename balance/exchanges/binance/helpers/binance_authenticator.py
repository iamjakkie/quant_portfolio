from binance import Client

from base_model.exchange_helpers.authenticator import Authenticator

class BinanceAuthenticator(Authenticator):
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key
        self.client = Client

    def authenticate(self):
        return Client(self.api_key, self.secret_key)
        # print(self.client.get_account())

# def get_balance(api_key, api_secret):
#     client = Client(api_key, api_secret)
#     balance = client.get_asset_balance(asset='BTC')