import asyncio
import os

from balance.exchanges.kucoin.kucoin_client import Kucoin

async def main():
    credentials = {}

    api_key = os.environ["kucoin_api_key"]
    api_secret = os.environ["kucoin_api_secret"]
    api_passphrase = os.environ["kucoin_api_passphrase"]

    kucoin = Kucoin(api_key, api_secret, api_passphrase)

    # await kucoin.get_balance()
    # for currency, balance in kucoin.balances.items():
    #     print(f"{currency}: {float(balance):,.5f}")

    # await kucoin.get_tickers()
    # for currency, price in kucoin.last_tickers.items():
    #     print(f"{currency}: {float(price):,.5f}")

    counter = 0
    while True:
        if counter % 10 == 0:
            await kucoin.get_wallet()
        else:
            await kucoin.get_wallet(False)
        for currency, value in kucoin.wallet.items():
            print(f"{currency}: {float(value):,.5f}")
        print('======================')
        counter += 1

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())