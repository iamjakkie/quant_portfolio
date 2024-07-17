from CEFI.binance.binance_client import BinanceClient
from CEFI.coinbase.coinbase_client import CoinbaseClient
from CEFI.gate_io.gateio_client import GateIOClient

from coinbase.rest import RESTClient
from coinbase import jwt_generator

import asyncio
import json
import os

async def main():

    binance_client = BinanceClient(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_SECRET_KEY"))
    binance_bals = binance_client.get_balance()
    with open("cdp_api_key.json", "r") as f:
        key_data = json.load(f)
    coinbase_client = CoinbaseClient(key_data["name"], key_data["privateKey"])
    coinbase_bals = await coinbase_client.get_account()
    gateio_client = GateIOClient(os.getenv("GATEIO_API_KEY"), os.getenv("GATEIO_SECRET_KEY"))
    gateio_bals = await gateio_client.get_account()

    balances_combined = binance_bals + coinbase_bals + gateio_bals
    for bal in balances_combined:
        print(bal)
    

if __name__ == "__main__":
    asyncio.run(main())