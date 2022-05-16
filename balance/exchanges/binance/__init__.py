import asyncio

from balance.exchanges.binance.binance_client import Binance

async def main():
    credentials = {}
    with open('/workspaces/quant_earnings/balance/exchanges/binance/credentials.txt', 'r') as creds:
        for line in creds.readlines():
            key, value = line.split('=')
            credentials[key] = value.replace('\n', '')
    
    binance = Binance(credentials['api_key'], credentials['api_secret'])
    await binance.get_balance()
    for currency, balance in binance.balances.items():
        print(f"{currency}: {float(balance):,.5f}")


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())