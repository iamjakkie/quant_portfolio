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
SKIP_CURRENCIES = ['USDT']

class GateioConnector(Connector):
    def __init__(self, auth: GateioAuthenticator):
        self._auth = auth
        self.headers = auth.authenticate()
        self.balances = {}
        self.currencies = []
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
        self.currencies = []
        for row in resp_json:
            unit = BalanceUnit('Gateio', ts, row['currency'], row['available'])
            self.currencies.append(unit.currency)
            self.balances[unit.currency] = float(unit.balance)

    async def get_historical_trades(self):
        host = "https://api.gateio.ws"
        url = '/api/v4/spot/my_trades'
        for currency in self.currencies:
            query_param = 'currency_pair={}_USDT'.format(currency)
            print(query_param)
            async with aiohttp.ClientSession() as client:
                headers = {'Accept': 'application/json', 
                        'Content-Type': 'application/json'}
                sign_headers = self._auth.gen_sign('GET', host + url, query_param)
                headers.update(sign_headers)
                resp = await client.get(host + url + "?" + query_param, headers=headers)
                resp_json = await resp.json()
                print(resp_json)
            #response = await requests.request('GET', host + url, headers=self.headers)
            if resp.status != 200:
                # TODO proper error handling
                raise "error"
            for row in resp_json:
                print(row)
        
    def get_currencies(self):
        pass


    async def subscribe_ws(self):
        self._ws = await websockets.connect(WS_URL)
        params = {
            "time": int(time.time()),
            "channel": "spot.tickers",
            "event": "subscribe",
            "payload": [currency+"_USDT" for currency in self.currencies if currency not in SKIP_CURRENCIES]
        }
        # params['auth'] = self._auth.gen_sign(params['channel'], params['event'], params['time'])
        print(params)
        await self._ws.send(json.dumps(params))
        
        while True:
            try:
                res = await asyncio.wait_for(self._ws.recv(), 30.)
                try:
                    msg = json.loads(res)

                    # API errors
                    if msg.get('error', None) is not None:
                        error = msg.get('error', {}).get('message', msg['error'])
                        print(error)
                    
                    # subscribe/unsubscribe
                    event = msg.get('event')
                    if event == 'subscribe':
                        status = msg.get('result', {}).get('status')
                        if status == 'success':
                            print('Subscribed successfully')
                        yield None
                    elif event == 'unsubscribe':
                        status = msg.get('result', {}).get('status')
                        if status == 'success':
                            print('Unsubscribed successfully')
                        yield None
                    else:
                        try:
                            currency = msg['result']['currency_pair'].replace('_USDT','')
                            balance = float(msg['result']['last'])*self.balances[currency]
                            self.balances[currency] = balance
                        except Exception as e:
                            print(e)
                except ValueError:
                    continue
            except asyncio.TimeoutError:
                await asyncio.wait_for(self._ws.ping(), 10.)
            finally:
                pass

    def get_value(self):
        pass
