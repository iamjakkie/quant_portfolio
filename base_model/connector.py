import websockets
import pandas as pd

from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal




class Connector(ABC):
    
    @abstractmethod
    def get_balance():
        pass

    @abstractmethod
    def get_currencies():
        pass

    @abstractmethod
    async def subscribe_ws() -> websockets.WebSocketClientProtocol:
        pass

    @abstractmethod
    def get_value():
        pass

@dataclass
class BalanceUnit(ABC):
    exchange: str
    timestamp: pd.Timestamp
    currency: str
    balance: Decimal

    def __repr__(self):
        return '{}: Balance for {} in time {} is {}'.format(self.exchange, self.currency, self.timestamp, self.balance)