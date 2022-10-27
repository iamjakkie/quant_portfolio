import pandas as pd
from base_model.exchange import Exchange
from balance.exchanges.binance.helpers.binance_authenticator import BinanceAuthenticator
from balance.exchanges.binance.helpers.binance_connector import BinanceConnector


class Binance(Exchange):
    def __init__(self, key, secret):
        self._authenticator = BinanceAuthenticator(key, secret)
        self._connector = BinanceConnector(self._authenticator)
        self.balances = {}
        self.historical_trades = {}
        self.last_tickers = {}
        self.wallet = {}

    async def get_balance(self):
        units = await self._connector.get_balance()
        for unit in units:
            self.balances[unit.currency]=unit.balance

    # async def get_historical_trades(self):
    #     historical_trades = await self._connector.get_historical_trades()
    #     for currency, trades in historical_trades:
    #         self.historical_trades[currency]=trades

    async def get_tickers(self):
        self.last_tickers = await self._connector.get_tickers()
        # self.last_tickers = last_tickers

    async def get_wallet(self, refresh=True):
        #todo if there is no refresh - get the last currencies list
        if refresh:
            await self.get_balance()
        await self.get_tickers()
        for currency, balance in self.balances.items():
            # print(self.last_tickers.get(currency,[{'last':1}])[0]['last'])
            value = float(self.last_tickers.get(currency, 1))*float(balance)
            if value > 1.0:
                self.wallet[currency] = value
        return {'exchange': [self]*len(self.wallet.keys()), 
                'symbol': list(self.wallet.keys()), 
                'amount': list(self.balances.values()), 
                'value': list(self.wallet.values())}

    async def get_total(self, refresh=True):
        all_assets = await self.get_wallet(refresh)
        return sum(all_assets["value"])

    def __repr__(self) -> str:
        return 'Binance'