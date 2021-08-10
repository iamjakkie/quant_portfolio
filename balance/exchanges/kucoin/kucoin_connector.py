import requests
import pandas as pd
from decimal import Decimal

from kucoin_authenticator import KucoinAuthenticator
from base_model.connector import Connector, BalanceUnit

class KucoinConnector(Connector):
    def __init__(self, auth: KucoinAuthenticator):
        self.headers = auth.authenticate()

    async def get_balance(self):
        url = 'https://api.kucoin.com/api/v1/accounts'
        response = await requests.request('GET', url, headers=self.headers)
        if response.status_code != 200:
            # TODO proper error handling
            raise "error"
        rows = response.json()['data']
        ts = pd.Timestamp.utcnow().replace(second=0, microsecond=0)
        self.balance_list = []
        for row in rows:
            if row['type'] == 'trade':
                unit = BalanceUnit('Kucoin', row['currency'], ts, row['balance'])
                self.balance_list.append(unit)

        return self.balance_list

    def get_currencies(self):
        return [unit.currency for unit in self.balance_list]
        