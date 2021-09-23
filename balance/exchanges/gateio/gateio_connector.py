import requests
import pandas as pd 
import asyncio
import aiohttp
import websockets
import time
import json

from gateio_authenticator import GateioAuthenticator
from base_model.connector import Connector, BalanceUnit

WS_URL = "wss://api.gateio.ws/ws/v4/"

class GateioConnector(Connector):
    def __init__(self, auth: GateioAuthenticator):
        self._auth = auth
        self.headers = auth.authenticate()
        self.balance_list = []
        self.currencies = None
        self._ws = None

    async def get_balance(self):
        host = "https://api.gateio.ws"
        url = '/api/v4/spot/accounts'
        async with aiohttp.ClientSession() as client:
            resp = await client.get(host+url, headers=self.headers)
            resp_json = await resp.json()
        #response = await requests.request('GET', host + url, headers=self.headers)
        if resp.status != 200:
            # TODO proper error handling
            raise "error"
        #rows = response.json()
        ts = pd.Timestamp.utcnow().replace(second=0, microsecond=0)
        self.balance_list = []
        for row in resp_json:
            unit = BalanceUnit('Gateio', ts, row['currency'], row['available'])
            self.balance_list.append(unit.currency)
        
    def get_currencies(self):
        self.currencies = {unit.currency for unit in self.balance_list}


    async def subscribe_ws(self):
        self._ws = await websockets.connect(WS_URL)
        params = {
            "time": int(time.time()),
            "channel": "spot.balances",
            "event": "subscribe",
        }
        if self.currencies:
            params["payload"] = list(self.currencies) 
        params['auth'] = self._auth.gen_sign(params['channel'], params['event'], params['time'])
        await self._ws.send(json.dumps(params))
        
        if res['result']['status'] == 'success':
            while True:
                try:
                    res = await self._ws.recv()
                    pass
                except:
                    return
                finally:
                    pass

    def get_value(self):
        pass
