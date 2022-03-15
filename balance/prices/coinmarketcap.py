import aiohttp
import asyncio
import pandas as pd

from base_model.price_provider import PriceProvider, Price

class CoinMarketCap(PriceProvider):
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        self.map_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
        self.headers = {
            'Accepts':'application/json',
            'X-CMC_PRO_API_KEY':api_key
        }
        
    async def get_current_price(self, crypto):
        #TODO: split
        map_parameters = {
            'symbol':crypto
        }
        async with aiohttp.ClientSession() as client:
            resp = await client.get(self.map_url, headers=self.headers, params=map_parameters)
            resp_json = await resp.json()
        if resp.status != 200:
            raise IOError(f"Error fetching current price for {crypto}",
                            f"HTTP status: {resp.status}")
        id = resp_json['data'][0]['id']
        
        parameters = {
            'id': id,
            'convert': 'USD'
        }
        
        async with aiohttp.ClientSession() as client:
            resp = await client.get(self.url, headers=self.headers, params=parameters)
            resp_json = await resp.json()
        if resp.status != 200:
            print(resp)
            raise resp
        else:
            ts = pd.Timestamp.utcnow()#.replace(second=0, microsecond=0)
            return Price('coinmarketcap', ts, crypto, resp_json['data'][str(id)]['quote']['USD']['price'])