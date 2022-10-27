import asyncio
import time

import pandas as pd
from balance.balances import Balances

async def main():
    credentials = {}
    # with open('/workspaces/quant_earnings/balance/exchanges/kucoin/credentials.txt', 'r') as creds:
    #     for line in creds.readlines():
    #         key, value = line.split('=')
    #         credentials[key] = value.replace('\n', '')

    balances = Balances(['kucoin', 'gateio', 'binance'])

    # await kucoin.get_balance()
    # for currency, balance in kucoin.balances.items():
    #     print(f"{currency}: {float(balance):,.5f}")

    # await kucoin.get_tickers()
    # for currency, price in kucoin.last_tickers.items():
    #     print(f"{currency}: {float(price):,.5f}")
    
    # await balances.print_wallets()
    # res_df = await balances.get_wallets()
    # res = await balances.get_wallets()
    # print(res)
    counter = 0
    while True:
        if counter % 10 == 0:
            total = await balances.get_wallets_total()
        else:
            total = await balances.get_wallets_total(False)
        print(total)
        time.sleep(2)
        counter+=1
    return
    counter = 0
    while True:
        print(res)
        if counter % 10 == 0:
            # df = await balances.get_wallets()
            res = await balances.get_wallets()
        else:
            # df = await balances.get_wallets(False)
            res = await balances.get_wallets(False)
        # res_df = pd.concat([res_df, df])
        print('======================')
        counter += 1

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())