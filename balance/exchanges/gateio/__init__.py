from gateio_authenticator import GateioAuthenticator
from gateio_connector import GateioConnector

credentials = {}
with open('/workspaces/quant_earnings/balance/exchanges/gateio/credentials.txt', 'r') as creds:
    for line in creds.readlines():
        key, value = line.split('=')
        credentials[key] = value.replace('\n', '')

auth = GateioAuthenticator(credentials['api_key'], credentials['api_secret'])
gateio_connector = GateioConnector(auth)
gateio_connector.get_balance()