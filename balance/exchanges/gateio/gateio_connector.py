import requests
import pandas as pd 

from gateio_authenticator import GateioAuthenticator
from base_model.connector import Connector, BalanceUnit

class GateioConnector(Connector):
    def __init__(self, auth: GateioAuthenticator):
        self.headers = auth.authenticate()

    async def get_balance(self):
        host = "https://api.gateio.ws"
        url = '/api/v4/spot/accounts'
        response = await requests.request('GET', host + url, headers=self.headers)
        if response.status_code != 200:
            # TODO proper error handling
            raise "error"
        rows = response.json()
        ts = pd.Timestamp.utcnow().replace(second=0, microsecond=0)
        balance_list = []
        for row in rows:
            unit = BalanceUnit('Gateio', row['currency'], ts, row['available'])
            balance_list.append(unit)
        
    

    