from BASE_MODEL.balancer import BalanceUnit, ExchangeBalance
from CEFI.coinbase.helpers.coinbase_connector import CoinbaseConnector
from datetime import datetime

class CoinbaseClient():
    def __init__(self, key_name: str, secret_key: str):
        self.connector = CoinbaseConnector(key_name, secret_key)

    async def get_account(self):
        balances = []
        accounts = await self.connector.get_response("/accounts")
        accounts = accounts["accounts"]
        for wallet in accounts:
            currency = wallet["currency"]
            balance = wallet["available_balance"]["value"]
            if float(balance) > 0:
                bu = BalanceUnit(
                    datetime.now(),
                    currency,
                    float(balance)
                )
                balances.append(ExchangeBalance(
                    'COINBASE',
                    bu
                ))
        return balances

