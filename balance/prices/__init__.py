import asyncio 

from coinmarketcap import get_current_price

credentials = {}
with open('/workspaces/quant_earnings/balance/prices/credentials.txt') as creds:
    for line in creds.readlines():
        key, value = line.split('=')
        credentials[key] = value.replace('\n','')

asyncio.get_event_loop().run_until_complete(get_current_price(credentials['api_key'],'DOGE'))
