import pandas as pd
from base_model.exchange import Exchange
from balance.exchanges.kucoin.helpers.kucoin_authenticator import KucoinAuthenticator
from balance.exchanges.kucoin.helpers.kucoin_connector import KucoinConnector


class Kucoin(Exchange):
    def __init__(self, key, secret, api_pass):
        self._authenticator = KucoinAuthenticator(key, secret, api_pass)
        self._connector = KucoinConnector(self._authenticator)
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
        if refresh:
            await self.get_balance()
        await self.get_tickers()
        for currency, balance in self.balances.items():
            # print(self.last_tickers.get(currency,[{'last':1}])[0]['last'])
            self.wallet[currency] = float(self.last_tickers.get(currency,1))*float(balance)

        return {'exchange': [self]*len(self.wallet.keys()), 
                'symbol': list(self.wallet.keys()), 
                'amount': list(self.balances.values()), 
                'value': list(self.wallet.values())}

    # async def print_wallet(self):
    #     for currency, value in self.wallet.items():
    #         print(f"{currency}: {float(value):,.5f}")

    def __repr__(self) -> str:
        return 'Kucoin'