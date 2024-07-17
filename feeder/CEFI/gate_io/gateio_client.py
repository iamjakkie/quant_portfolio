from BASE_MODEL.balancer import BalanceUnit, ExchangeBalance
from CEFI.gate_io.helpers.gateio_connector import GateIOConnector

from datetime import datetime

class GateIOClient():
    def __init__(self, api_key: str, secret_key: str):
        self.connector = GateIOConnector(api_key, secret_key)

    async def get_account(self):
        balances = []
        small_balances = await self.connector.get_response("/wallet/small_balance")
        for bal in small_balances:
            if float(bal["available_balance"]) > 0:
                bu = BalanceUnit(
                    datetime.now(),
                    bal["currency"],
                    float(bal["available_balance"])
                )
                balances.append(ExchangeBalance(
                    'GATE_IO',
                    bu
                ))
        return balances