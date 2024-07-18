from BASE_MODEL.balancer import BalanceUnit, ExchangeBalance
from DEFI.etherscan.helpers.etherscan_connector import EtherscanConnector
from datetime import datetime

class EtherscanClient():
    def __init__(self, api_key: str):
        self.connector = EtherscanConnector(api_key)
    
    async def __get_ether_balance(self, address: str):
        url_kv = {
            "module": "account",
            "action": "balance",
            "address": address,
            "tag": "latest"
        }
        balance = await self.connector.get_response(url_kv)
        return balance["result"]

    async def __get_token_balances(self, address: str):
        url_kv = {
            "module": "account",
            "action": "addresstokenbalance",
            "address": address,
            "page": 1,
            "offset": 100,
        }
        balance = await self.connector.get_response(url_kv)
        return balance["result"]

    async def get_account(self, address: str):
        balances = []
        eth_balance = await self.__get_ether_balance(address)
        bu = BalanceUnit(
            datetime.now(),
            "ETH",
            eth_balance
        )
        balances.append(ExchangeBalance(
            'ETHERSCAN',
            bu
        ))
        token_balances = await self.__get_token_balances(address)
        for token in token_balances:
            bu = BalanceUnit(
                datetime.now(),
                f'{token["TokenAddress"]} {token["TokenSymbol"]}',
                int(token["TokenQuantity"])/int(token["TokenDivisor"])
            )
            balances.append(ExchangeBalance(
                'ETHERSCAN',
                bu
            ))
        return balances