from BASE_MODEL.balancer import BalanceUnit, ExchangeBalance
from CEFI.binance.helpers.binance_connector import BinanceConnector
from datetime import datetime

class BinanceClient():
    def __init__(self, api_key: str, secret_key: str):
        self.connector = BinanceConnector(api_key, secret_key)

    def _get_balance(self):
        raw_assets = self.connector.get_account()["balances"]
        for raw_asset in raw_assets:
            if float(raw_asset['free']) > 0:
                bu = BalanceUnit(
                    datetime.now(),
                    raw_asset['asset'],
                    float(raw_asset['free'])
                )
                yield ExchangeBalance(
                    'BINANCE',
                    bu
                )

    def get_balance(self):
        return list(self._get_balance())