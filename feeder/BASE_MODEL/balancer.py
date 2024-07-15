from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List

@dataclass
class BalanceUnit(ABC):
    timestamp: datetime
    currency: str
    balance: Decimal

    def __repr__(self):
        return 'Balance for {} in time {} is {}'.format(self.currency, self.timestamp, self.balance)
    
@dataclass
class ExchangeBalance:
    exchange: str
    BU: BalanceUnit

class Balance(ABC):
    totalBalances: List[ExchangeBalance]

    @abstractmethod
    def get_trading_pairs(self):
        pass