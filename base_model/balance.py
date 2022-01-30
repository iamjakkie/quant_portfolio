import pandas as pd
from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal
from connector import BalanceUnit


class Balance(ABC):
    totalBalances: []

    @abstractmethod
    def get_trading_pairs():
        pass


@dataclass
class ExchangeBalance:
    exchange: str
    BU: BalanceUnit