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
        print(x)
        try:
            doge_id = await coinmarketcap_provider.get_mapping('DOGE')
            doge = await coinmarketcap_provider.get_current_price(doge_id)
            print(doge)
            sleep(1)
        except Exception:
            await asyncio.sleep(5)
        finally:
            x+=1

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())