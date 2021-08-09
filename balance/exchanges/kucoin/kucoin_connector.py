import requests
import pandas as pd
from decimal import Decimal

from kucoin_authenticator import KucoinAuthenticator
from base_model.connector import Connector, BalanceUnit

class KucoinConnector(Connector):
    def __init__(self, auth: KucoinAuthenticator):
        self.headers = auth.authenticate()

    def get_balance(self):
        url = 'https://api.kucoin.com/api/v1/accounts'
        response = requests.request('GET', url, headers=self.headers)
        if response.status_code != 200:
            # TODO proper error handling
            raise "error"
        rows = response.json()['data']
        for row in rows:
            if row['type'] == 'trade':
                unit = BalanceUnit('Kucoin', row['currency'], pd.Timestamp.utcnow().replace(minute=0, second=0, microsecond=0), row['balance'])
                print(unit)
        