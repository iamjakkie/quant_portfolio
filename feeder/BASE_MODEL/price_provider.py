import pandas as pd

from decimal import Decimal
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Price(ABC):
    provider: str
    timestamp: str
    currency: str
    USD: Decimal

    def __repr__(self) -> str:
        return f'Provider: {self.provider} at {self.timestamp} for {self.currency}: {self.USD:.4f}$'

class PriceProvider(ABC):
    @abstractmethod
    def __init__(self, api_key:str) -> None:
        self._api_key = api_key
    
    @abstractmethod
    async def get_price(self, asset:str) -> Price:
        pass
    
    @abstractmethod
    async def get_historical_prices(self, asset:str, start:pd.Timestamp, end:pd.Timestamp=None) -> [Price]:
        pass

