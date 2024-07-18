from BASE_MODEL.connector import Connector
from DEFI.etherscan.helpers.etherscan_authenticator import EtherscanAuthenticator

import aiohttp
import asyncio 

BASE_URL = "https://api.etherscan.io/api?"

class EtherscanConnector(Connector):
    def __init__(self, api_key: str):
        self.__auth = EtherscanAuthenticator(api_key)

    def __get_headers(self, url:str):
        return self.__auth.authenticate(url)
    
    async def get_response(self, url_kv):
        path = "&".join([f"{k}={v}" for k, v in url_kv.items()])
        url = f"{BASE_URL}{path}"
        url = self.__get_headers(url)
        async with aiohttp.ClientSession(timeout=None) as client:
            res = await client.get(url)
            await asyncio.sleep(0.001)
            while res.status != 200:
                if res.status == 401:
                    print(res.text)
                    print(res.json())
                    client = aiohttp.ClientSession()
                await asyncio.sleep(5)
                res = await client.get(url)
                await asyncio.sleep(0.001)
            try:
                resp = await res.json(content_type=None)
            except Exception as e:
                print(await res.text())
                print(e)
        return resp
