import pandas as pd

from decimal import Decimal
from abc import ABC, abstractmethod
from dataclasses import dataclass

class PriceProvider(ABC):
    @abstractmethod
    def __init__(self, api_key) -> None:
        super().__init__()
    
    @abstractmethod
    async def get_current_price(self, crypto):
        ...

@dataclass
class Price(ABC):
    provider: str
    timestamp: pd.Timestamp
    currency: str
    USD: Decimal

    def __repr__(self) -> str:
        return f'Provider: {self.provider} at {self.timestamp} for {self.currency}:{self.USD:.4f}$'