
from FEEDER.BASE_MODEL.connector import Connector, BalanceUnit
from CEFI.binance.helpers.binance_authenticator import BinanceAuthenticator

class BinanceConnector():
    def __init__(self, auth: BinanceAuthenticator):
        # self._auth = auth
        self.client = auth.authenticate()

    def get_account(self):
        return self.client.get_account()
        