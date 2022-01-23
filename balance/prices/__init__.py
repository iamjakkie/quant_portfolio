import asyncio 

from coinmarketcap import get_current_price

asyncio.get_event_loop().run_until_complete(get_current_price('dogecoin'))
