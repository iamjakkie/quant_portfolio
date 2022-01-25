import pandas as pd
from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal

class Balance(ABC):

    @abstractmethod
    def get_trading_pairs():
        pass


@dataclass
class ExchangeBalanceUnit