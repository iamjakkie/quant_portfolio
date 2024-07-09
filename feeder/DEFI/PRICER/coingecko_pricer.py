from FEEDER.BASE_MODEL.price_provider import PriceProvider, Price

## imports
import aiohttp
import asyncio
import time

## implementation
class CoinGecko(PriceProvider):
    def __init__(self, api_key:str=None) -> None:
        self._api_key = api_key
        self._header = self.generate_header()
        self.base_url = "https://pro-api.coingecko.com/api/v3"

    def generate_header(self) -> dict:
        header = {
            'Accepts':'application/json'
        }
        if self._api_key:
            header['x-cg-pro-api-key'] = self._api_key
        return header
    
    async def get_price(self, asset_str:str) -> Price:
        """
        assumption: all data until yesterday is in the database
        """
        date = time.strftime("%d-%m-%Y")
        url = f"{self.base_url}/coins/{asset_str}/history?date={date}"
        async with aiohttp.ClientSession() as client:
            resp = await client.get(url, headers=self._header)

        resp_json = await resp.json()
        await asyncio.sleep(0.2)
        try:
            prices = resp_json['market_data']['current_price']
        except Exception as e:
            print(f"Error fetching price for {asset_str}")
            print(e)
            return None
        return Price('coingecko', date, asset_str, prices['usd'])


    async def get_historical_prices(self, asset_str:str) -> [Price]:
        """
        assumption: no data is in the database, get everything until yesterday
        """
        pass