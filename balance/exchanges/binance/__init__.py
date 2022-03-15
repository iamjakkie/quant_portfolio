import asyncio

from binance_authenticator import BinanceAuthenticator
from binance_connector import BinanceConnector

async def main():
    credentials = {}
    with open('/workspaces/quant_earnings/balance/exchanges/binance/credentials.txt', 'r') as creds:
        for line in creds.readlines():
            key, value = line.split('=')
            credentials[key] = value.replace('\n', '')
    
    auth = BinanceAuthenticator(credentials['api_key'], credentials['api_secret'])
    binance_connector = BinanceConnector(auth)
    await binance_connector.get_balance()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())