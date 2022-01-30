

from binance_authenticator import BinanceAuthenticator
from base_model.connector import Connector, BalanceUnit

URL = ""

class BinanceConnector(Connector):
    def __init__(self, auth: BinanceAuthenticator):
        self._auth = auth
        self.client = auth.authenticate()
        self.balances = {}
        self.currencies = []
        
    async def get_balance(self):
        print(type(self.client.get_account()))
        # self.client.get_account(self)
        # res = await self._auth.client.get_account(self._auth)
        # print(res)
        # pass

    async def get_currencies(self):
        pass

    async def subscribe_ws(self):
        pass

    def get_value(self):
        pass

    def get_balance_units():
        pass