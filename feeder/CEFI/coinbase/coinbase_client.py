from BASE_MODEL.balancer import BalanceUnit, ExchangeBalance
from CEFI.coinbase.helpers.coinbase_connector import CoinbaseConnector
from datetime import datetime

class CoinbaseClient():
    def __init__(self, key_name: str, secret_key: str):
        self.connector = CoinbaseConnector(key_name, secret_key)

    async def get_account(self):
        return await self.connector.get_response("/accounts")
