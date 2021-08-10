import asyncio
import aiohttp

from gateio_authenticator import GateioAuthenticator
from gateio_connector import GateioConnector



def main():
    credentials = {}
    with open('/workspaces/quant_earnings/balance/exchanges/gateio/credentials.txt', 'r') as creds:
        for line in creds.readlines():
            key, value = line.split('=')
            credentials[key] = value.replace('\n', '')

    auth = GateioAuthenticator(credentials['api_key'], credentials['api_secret'])

    gateio_connector = GateioConnector(auth)
    asyncio.get_event_loop().run_until_complete(gateio_connector.get_balance())
    print(gateio_connector.balance_list)
    
    async with aiohttp.ClientSession() as client:
            header = self._kucoin_auth.add_auth_to_params("POST", KUCOIN_USER_STREAM_ENDPOINT)
            async with client.post(f"{KUCOIN_API_ENDPOINT}{KUCOIN_USER_STREAM_ENDPOINT}", headers=header) as response:
                response: aiohttp.ClientResponse = response
if __name__ == '__main__':
    main()