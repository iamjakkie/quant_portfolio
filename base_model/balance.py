from abc import ABC, abstractmethod

class Balance(ABC):

    @abstractmethod
    def get_trading_pairs():
        