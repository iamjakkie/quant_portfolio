import websockets
import pandas as pd

from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal




class Connector(ABC):
    balances = {}
    
    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_currencies(self):
        pass

    @abstractmethod
    async def subscribe_ws(self) -> websockets.WebSocketClientProtocol:
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_balance_units(self):
        pass

@dataclass
class BalanceUnit(ABC):
    # exchange: str
    timestamp: pd.Timestamp
    currency: str
    balance: Decimal

    def __repr__(self):
        return '{}: Balance for {} in time {} is {}'.format(self.exchange, self.currency, self.timestamp, self.balance)