import requests
import pandas as pd 
import asyncio
import aiohttp
import websockets
import time
import json

from websocket import create_connection
from gateio_authenticator import GateioAuthenticator
from base_model.connector import Connector, BalanceUnit

class GateioConnector(Connector):
    def __init__(self, auth: GateioAuthenticator):
        self.headers = auth.authenticate()
        self.balance_list = []

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
        return {unit.currency for unit in self.balance_list}


    def subscribe_ws(self) -> websockets.WebSocketClientProtocol:
        ws = create_connection("wss://api.gateio.ws/ws/v4/")
        request = {
            "time": int(time.time()),
            "channel": "spot.balances",
            "event": "subscribe",  # "unsubscribe" for unsubscription
        }
        request['auth'] = self.headers
        ws.send(json.dumps(request))
        print(ws.recv())

    def get_value(self):
        pass
