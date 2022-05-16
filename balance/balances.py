# from base_model.exchange_helpers.balance import Balance
import os
import pandas as pd
from balance.exchanges.kucoin import Kucoin
from balance.exchanges.gateio import GateIO
from balance.exchanges.binance import Binance

class Balances():
    def __init__(self, exchanges) -> None:
        self._exchanges_client_map = {'binance': Binance,
                                    'gateio': GateIO,
                                    'kucoin': Kucoin}
        self._exchanges_req_map = {'binance': ['binance_api_key','binance_api_secret'],
                'gateio': ['gateio_api_key', 'gateio_api_secret'],
                'kucoin': ['kucoin_api_key', 'kucoin_api_secret', 'kucoin_api_passphrase']}
        self.wallets = []
        self.exchanges = []
        for exchange in exchanges:
            self.exchanges.append(self._exchanges_client_map[exchange](*[os.environ[key] for key in self._exchanges_req_map[exchange]]))

    async def get_wallets(self, refresh=True):
        for exchange in self.exchanges:
            await exchange.get_wallet(refresh)
            self.wallets.append(exchange.wallet)
    
    async def print_wallets(self):
        display(df)
        # for exchange in self.exchanges:
        #     for currency, value in exchange.wallet.items():
        #         print(f"{exchange}_{currency}: {float(value):,.5f}")