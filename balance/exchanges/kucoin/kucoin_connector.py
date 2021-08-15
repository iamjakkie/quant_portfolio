import requests
import pandas as pd
import asyncio
import aiohttp
from decimal import Decimal

from kucoin_authenticator import KucoinAuthenticator
from base_model.connector import Connector, BalanceUnit

class KucoinConnector(Connector):
    def __init__(self, auth: KucoinAuthenticator):
        self.headers = auth.authenticate()

    async def get_balance(self):
        url = 'https://api.kucoin.com/api/v1/accounts'
        async with aiohttp.ClientSession() as client:
            resp = await client.get(url, headers=self.headers)
            resp_json = await resp.json()
        if resp.status != 200:
            # TODO proper error handling
            raise "error"
        rows = resp_json['data']
        ts = pd.Timestamp.utcnow().replace(second=0, microsecond=0)
        self.balance_list = set()
        for row in rows:
            if row['type'] == 'trade':
                unit = BalanceUnit('Kucoin', ts, row['currency'], row['balance'])
                self.balance_list.add(unit.currency)

        return self.balance_list

    def get_currencies(self):
        print(type({unit.currency for unit in self.balance_list}))
        return {unit.currency for unit in self.balance_list}

    def subscribe_ws(self):
        pass

    def get_value(self):
        pass

        