from BASE_MODEL.balancer import BalanceUnit, ExchangeBalance
from CEFI.gate_io.helpers.gateio_connector import GateIOConnector

class GateIOClient():
    def __init__(self, api_key: str, secret_key: str):
        self.connector = GateIOConnector(api_key, secret_key)

    async def get_account(self):
        print('get_account')
        return await self.connector.get_response("/wallet/small_balance")