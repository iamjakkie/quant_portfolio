import asyncio

from balance.exchanges.gateio import GateioAuthenticator, GateioConnector
from balance.exchanges.kucoin import KucoinAuthenticator, KucoinConnector
from balance.exchanges.binance import BinanceAuthenticator, BinanceConnector
from balance.prices.coinmarketcap import CoinMarketCap

async def main():
    credentials = {}
    with open('/workspaces/quant_earnings/balance/credentials.txt') as creds:
        for line in creds.readlines():
            key, value = line.split('=')
            credentials[key] = value 
    
    
    

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
