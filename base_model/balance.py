import pandas as pd
from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal
from connector import BalanceUnit
from types import List

@dataclass
class ExchangeBalance:
    exchange: str
    BU: BalanceUnit

class Balance(ABC):
    totalBalances: List[ExchangeBalance]

    @abstractmethod
    def get_trading_pairs(self):
        pass
