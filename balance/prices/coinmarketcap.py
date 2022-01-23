import aiohttp
import asyncio

async def get_current_price(api_key, crypto):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    
    
    map_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    map_parameters = {
        'symbol':crypto
    }
    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':api_key
    }
    async with aiohttp.ClientSession() as client:
        resp = await client.get(map_url, headers=headers, params=map_parameters)
        resp_json = await resp.json()
    if resp.status != 200:
        raise 'error'
    id = resp_json['data'][0]['id']
    
    parameters = {
        'id': id,
        'convert': 'USD'
    }

    
    async with aiohttp.ClientSession() as client:
        resp = await client.get(url, headers=headers, params=parameters)
        resp_json = await resp.json()
    if resp.status != 200:
        raise 'error'
    # price = resp_json['quote']['USD']['price']
    print(f"Price: {resp_json['data'][str(id)]['quote']['USD']['price']}")
