from FEEDER.BASE_MODEL.price_provider import PriceProvider, Price

## imports
import aiohttp
import asyncio
import datetime
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
    
    async def get_price(self, asset_str:str, date:str=None) -> Price:
        """
        assumption: all data until yesterday is in the database
        """
        if not date:
            date = time.strftime("%d-%m-%Y")
        url = f"{self.base_url}/coins/{asset_str}/history?date={date}"
        async with aiohttp.ClientSession() as client:
            async with client.get(url, headers=self._header) as resp:
                resp_json = await resp.json(content_type=None)
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
        args = []
        starting_date = datetime.datetime(2024, 1, 1).date()
        current_date = datetime.date.today()
        missing_dates = (current_date - starting_date).days
        for i in range(missing_dates+1):
            date = starting_date + datetime.timedelta(days=i)
            args.append(date.strftime("%d-%m-%Y"))
        prices = await asyncio.gather(*[self.get_price(asset_str, date) for date in args])
        return prices