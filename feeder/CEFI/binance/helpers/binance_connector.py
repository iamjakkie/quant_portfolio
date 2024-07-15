
from BASE_MODEL.connector import Connector
from CEFI.binance.helpers.binance_authenticator import BinanceAuthenticator

class BinanceConnector(Connector):
    def __init__(self, api_key: str, secret_key:str):
        auth = BinanceAuthenticator(api_key, secret_key)
        self.client = auth.authenticate()

    def get_account(self):
        return self.client.get_account()
        