import asyncio
import os

from balance.exchanges.binance.binance_client import Binance

async def main():
    api_key=os.environ["binance_api_key"]
    api_secret=os.environ["binance_api_secret"]
    
    binance = Binance(api_key, api_secret)
    # await binance.get_balance()
    # for currency, balance in binance.balances.items():
    #     print(f"{currency}: {float(balance):,.5f}")
    
    # await binance.get_tickers()
    # for currency, price in binance.last_tickers.items():
    #     print(f"{currency}: {float(price):,.5f}")

    counter = 0
    while True:
        if counter % 10 == 0:
            await binance.get_wallet()
        else:
            await binance.get_wallet(False)
        for currency, value in binance.wallet.items():
            print(f"{currency}: {float(value):,.5f}")
        print('======================')
        counter += 1


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())