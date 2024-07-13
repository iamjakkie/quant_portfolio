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
    async def subscribe_ws(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_balance_units(self):
        pass