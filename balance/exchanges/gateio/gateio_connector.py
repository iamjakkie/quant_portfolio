import requests

from gateio_authenticator import GateioAuthenticator
from base_model.connector import Connector

class GateioConnector(Connector):
    def __init__(self, auth: GateioAuthenticator):
        self.headers = auth.authenticate()

    def get_balance(self):
        host = "https://api.gateio.ws"
        url = '/api/v4/spot/accounts'
        response = requests.request('GET', host + url, headers=self.headers)
        print(response.status_code)
        return response.json()
        

    