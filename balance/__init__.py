import asyncio
import pandas as pd
from balance.balances import Balances

async def main():
    credentials = {}
    with open('/workspaces/quant_earnings/balance/exchanges/kucoin/credentials.txt', 'r') as creds:
        for line in creds.readlines():
            key, value = line.split('=')
            credentials[key] = value.replace('\n', '')

    balances = Balances(['binance', 'gateio', 'kucoin'])

    # await kucoin.get_balance()
    # for currency, balance in kucoin.balances.items():
    #     print(f"{currency}: {float(balance):,.5f}")

    # await kucoin.get_tickers()
    # for currency, price in kucoin.last_tickers.items():
    #     print(f"{currency}: {float(price):,.5f}")
    
    # await balances.print_wallets()
    res_df = await balances.get_wallets()
    counter = 0
    while True:
        print(res_df)
        if counter % 10 == 0:
            df = await balances.get_wallets()
        else:
            df = await balances.get_wallets(False)
        res_df = pd.concat([res_df, df])
        print('======================')
        counter += 1

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())