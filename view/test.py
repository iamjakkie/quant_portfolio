import asyncio
import pandas as pd
import plotly.offline as pyo
import plotly.express as px
from balance.balances import Balances


async def main():
    balances = Balances(['binance', 'gateio', 'kucoin'])

    # df = asyncio.run(balances.get_wallets())

    res_df = await balances.get_wallets()
    counter = 1
    while True:
        print(res_df)
        if counter % 10 == 0:
            df.to_csv('balances.csv', index=False)
            break
        else:
            df = await balances.get_wallets(False)
        res_df = pd.concat([res_df, df])
        print('======================')
        counter += 1

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

# fig = px.line(df, x='timestamp', y='value', line_group='symbol')
# pyo.plot(fig, filename='test.html')