from kucoin_connector import KucoinConnector
from kucoin_authenticator import KucoinAuthenticator

credentials = {}
with open('/workspaces/quant_earnings/balance/exchanges/kucoin/credentials.txt', 'r') as creds:
    for line in creds.readlines():
        key, value = line.split('=')
        credentials[key] = value.replace('\n', '')

auth = KucoinAuthenticator(credentials['api_key'], credentials['api_secret'], credentials['api_passphrase'])
kucoin_connector = KucoinConnector(auth)
kucoin_connector.get_balance()
print(kucoin_connector.balance_list)