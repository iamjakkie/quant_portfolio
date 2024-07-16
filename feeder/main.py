from CEFI.binance.binance_client import BinanceClient
from CEFI.coinbase.coinbase_client import CoinbaseClient

from coinbase.rest import RESTClient
from coinbase import jwt_generator

import asyncio
import json
import os

async def main():

    # binance_client = BinanceClient(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_SECRET_KEY"))
    # binance_bals = binance_client.get_balance()
    # for bal in binance_bals:
    #     print(bal)
    with open("cdp_api_key.json", "r") as f:
        key_data = json.load(f)
    coinbase_client = CoinbaseClient(key_data["name"], key_data["privateKey"])
    coinbase_bals = await coinbase_client.get_account()
    print(coinbase_bals)
    # for bal in coinbase_bals:
    #     print(bal)
    

if __name__ == "__main__":
    asyncio.run(main())