import aiohttp
import asyncio

async def get_current_price(crypto):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'slug': crypto,
        'convert': 'USD'
    }

    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':''
    }
    async with aiohttp.ClientSession() as client
    
    async with aiohttp.ClientSession() as client:
        resp = await client.get(url, headers=headers, params=parameters)
        resp_json = await resp.json()
    if resp.status != 200:
        raise 'error'
    # price = resp_json['quote']['USD']['price']
    print(f"Price: {resp_json['status']}")
