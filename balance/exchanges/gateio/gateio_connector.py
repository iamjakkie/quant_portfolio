import requests
import pandas as pd 

from gateio_authenticator import GateioAuthenticator
from base_model.connector import Connector, BalanceUnit

class GateioConnector(Connector):
    def __init__(self, auth: GateioAuthenticator):
        self.headers = auth.authenticate()

    def get_balance(self):
        host = "https://api.gateio.ws"
        url = '/api/v4/spot/accounts'
        response = requests.request('GET', host + url, headers=self.headers)
        if response.status_code != 200:
            # TODO proper error handling
            raise "error"
        rows = response.json()
        ts = pd.Timestamp.utcnow().replace(second=0, microsecond=0)
        for row in rows:
            unit = BalanceUnit('Gateio', row['currency'], ts, row['available'])
            print(unit)
        
    

    