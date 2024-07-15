from BASE_MODEL.authenticator import Authenticator

import aiohttp
import base64
import hashlib
import hmac
import time

URL = "https://api.exchange.coinbase.com"

async def get_server_timestamp():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}/time") as response:
            res_json = await response.json(content_type=None)
            return str(int(res_json["epoch"]))


class CoinbaseAuthenticator(Authenticator):
    def __init__(self, api_key: str, secret_key: str, passphrase: str):
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.__passphrase = passphrase

    async def authenticate(self, method: str, url: str, body: str = ""):
        try:
            self.now = await get_server_timestamp()
        except Exception as e:
            self.now = None
        if not self.now:
            self.now = str(int(time.time()))
        
        msg = (self.now + method.upper() + url + body).encode('ascii')
        hmac_key = base64.b64decode(self.__secret_key)
        signature = hmac.new(hmac_key, msg, hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')

        return {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Origin": "https://api.exchange.coinbase.com",
            "Content-Type": "application/json",
            "CB-ACCESS-SIGN": signature_b64,
            "CB-ACCESS-TIMESTAMP": self.now,
            "CB-ACCESS-PASSPHRASE": self.__passphrase,
            "CB-ACCESS-KEY": self.__api_key,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        }

    