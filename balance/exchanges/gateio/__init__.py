import asyncio

# from gateio_authenticator import GateioAuthenticator
# from gateio_connector import GateioConnector
from balance.exchanges.gateio.gateio_client import GateIO

async def main():
    credentials = {}
    with open('/workspaces/quant_earnings/balance/exchanges/gateio/credentials.txt', 'r') as creds:
        for line in creds.readlines():
            key, value = line.split('=')
            credentials[key] = value.replace('\n', '')

    gateio = GateIO(credentials['api_key'], credentials['api_secret'])
    # await gateio.get_balance()
    # for currency, balance in gateio.balances.items():
    #     print(f"{currency}: {float(balance):,.5f}")

    # await gateio.get_tickers()
    # for currency, last_ticker in gateio.last_tickers.items():
    #     print(f"{currency}: {last_ticker}")
    counter = 0
    while True:
        if counter % 10 == 0:
            await gateio.get_wallet()
        else:
            await gateio.get_wallet(False)
        for currency, value in gateio.wallet.items():
            print(f"{currency}: {float(value):,.5f}")
        print('======================')
        counter += 1
        # await asyncio.sleep(5)
    # await gateio.get_historical_trades()
    # for currency, trades in gateio.historical_trades.items():
    #     print(f"{currency}: {trades}")
    
    # async for balance in gateio.balances:
    #     await print(balance)
    # auth = GateioAuthenticator(credentials['api_key'], credentials['api_secret'])

    # gateio_connector = GateioConnector(auth)
    # await gateio_connector.get_balance()
    # # asyncio.get_event_loop().run_until_complete(gateio_connector.subscribe_ws())
    # print(gateio_connector.currencies)
    # await gateio_connector.get_historical_trades()
    # # async for i in gateio_connector.subscribe_ws():
    # #     print(i)
    # # async with aiohttp.ClientSession() as client:
    # #         header = self._kucoin_auth.add_auth_to_params("POST", KUCOIN_USER_STREAM_ENDPOINT)
    # #         async with client.post(f"{KUCOIN_API_ENDPOINT}{KUCOIN_USER_STREAM_ENDPOINT}", headers=header) as response:
    # #             response: aiohttp.ClientResponse = response

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())