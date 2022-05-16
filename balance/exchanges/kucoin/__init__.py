import asyncio

from balance.exchanges.kucoin.kucoin_client import Kucoin

async def main():
    credentials = {}
    with open('/workspaces/quant_earnings/balance/exchanges/kucoin/credentials.txt', 'r') as creds:
        for line in creds.readlines():
            key, value = line.split('=')
            credentials[key] = value.replace('\n', '')

    kucoin = Kucoin(credentials['api_key'], credentials['api_secret'], credentials['api_passphrase'])

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