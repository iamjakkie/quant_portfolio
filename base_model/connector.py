import pandas as pd

from dataclasses import dataclass
from decimal import Decimal

from abc import ABC, abstractmethod

class Connector(ABC):
    
    @abstractmethod
    def get_balance():
        pass

    @abstractmethod
    def get_currencies():
        pass

    @abstractmethod
    def subscribe_ws():
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