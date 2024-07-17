from BASE_MODEL.connector import Connector
from CEFI.gate_io.helpers.gateio_authenticator import GateIOAuthenticator

import aiohttp
import asyncio

BASE_URL = "https://api.gateio.ws/api/v4"

class GateIOConnector(Connector):
    def __init__(self, api_key: str, secret_key:str):
        self.__auth = GateIOAuthenticator(api_key, secret_key)

    def __get_headers(self, uri:str):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        headers.update(self.__auth.authenticate(uri))
        return headers

    async def get_response(self, path:str):
        uri = f"/api/v4{path}"
        url = f"{BASE_URL}{path}"
        print('get header')
        print(uri)
        header = self.__get_headers(uri=uri)
        print(header)
        print(url)
        async with aiohttp.ClientSession(headers=header, timeout=None) as client:
            res = await client.get(url)
            print(res.text)
            print(await res.json())
            await asyncio.sleep(0.001)
            while res.status != 200:
                if res.status == 401:
                    print(res.text)
                    print(res.json())
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