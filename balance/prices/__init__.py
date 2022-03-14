import asyncio 
from time import sleep
from coinmarketcap import CoinMarketCap

async def main():
    x = 0
    credentials = {}
    with open('/workspaces/quant_earnings/balance/prices/credentials.txt') as creds:
        for line in creds.readlines():
            key, value = line.split('=')
            credentials[key] = value.replace('\n','')

    coinmarketcap_provider = CoinMarketCap(credentials['api_key'])
    while(x < 121):
        doge = await coinmarketcap_provider.get_current_price('DOGE')
        print(doge)
        sleep(.5)
        x+=1

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())