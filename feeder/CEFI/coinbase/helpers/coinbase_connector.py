from BASE_MODEL.connector import Connector
from CEFI.coinbase.helpers.coinbase_authenticator import CoinbaseAuthenticator

import aiohttp
import asyncio

BASE_URL = "https://api.coinbase.com/api/v3/brokerage"

class CoinbaseConnector(Connector):
    def __init__(self, key_name:str, secret_key:str):
        self.__auth = CoinbaseAuthenticator(key_name, secret_key)

    def __get_headers(self, uri: str, body: str = "", method: str = "GET"):
        jwt_token = self.__auth.authenticate(uri)

        return {
            # "User-Agent": "coinbase-advanced-py/1.4.2",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {jwt_token}",
        }
        
    
    # async def get_response(self, url: str, method: str="get", body: str = ""):
    #     header = self.__get_headers(method, url, body)
    #     async with aiohttp.ClientSession(headers=header) as session:
    #         async with session.request(method, url, headers=header, data=body) as response:
    #             return await response.json(content_type=None)

    async def get_response(self, path: str, method:str = "GET", header=""):
        uri = f"{method} {BASE_URL}{path}".replace("https://" , "")
        url = f"{BASE_URL}{path}"
        if not header:
            header = self.__get_headers(uri=uri)
        print(header)
        async with aiohttp.ClientSession(headers=header, timeout=None) as client:
            res = await client.get(url)
            await asyncio.sleep(0.001)
            while res.status != 200:
                if res.status == 401:
                    print(res.text)
                    print(res.request_info)
                    header = self.__get_headers(uri=uri)
                    client = aiohttp.ClientSession(headers=header)
                await asyncio.sleep(5)
                res = await client.get(f"{url}")
                await asyncio.sleep(0.001)
            try:
                resp = await res.json(content_type=None)
            except Exception as e:
                print(await res.text())
                print(e)
        return resp
