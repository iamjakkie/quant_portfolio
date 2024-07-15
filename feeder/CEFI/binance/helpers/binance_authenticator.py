from binance import Client 
from BASE_MODEL.authenticator import Authenticator

class BinanceAuthenticator(Authenticator):
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key
        self.client = Client

    def authenticate(self):
        return Client(self.api_key, self.secret_key)