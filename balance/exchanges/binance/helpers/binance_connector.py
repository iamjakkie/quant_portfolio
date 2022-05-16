import pandas as pd
from balance.exchanges.binance.helpers.binance_authenticator import BinanceAuthenticator
from base_model.exchange_helpers.connector import Connector, BalanceUnit
from decimal import Decimal

URL = ""

class BinanceConnector(Connector):
    def __init__(self, auth: BinanceAuthenticator):
        self._auth = auth
        self.client = auth.authenticate()
        self.balances = {}
        self.currencies = []
        self.balance_units = []
        self.balance_units_currencies = {}
        self._ws = None

    async def get_balance(self):
        res = self.client.get_account()
        self.balance_list = set()
        units = []
        for curr in res['balances']:
            if(Decimal(curr['free']) > 0):
                ts = pd.Timestamp.utcnow().replace(second=0, microsecond=0)
                unit = BalanceUnit(ts, curr['asset'], curr['free'])
                self.balance_units.append(unit)
                self.balance_units_currencies[unit.currency] = unit 
                self.currencies.append(unit.currency)
                self.balances[unit.currency] = float(unit.balance)
                units.append(unit)
        return units

    async def get_tickers(self):
        
    
    async def get_currencies(self):
        pass

    async def subscribe_ws(self):
        pass

    def get_value(self):
        pass

    def get_balance_units():
        pass