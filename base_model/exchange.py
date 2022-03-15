from base_model.exchange_helpers.connector import Connector
from base_model.exchange_helpers.balance import Balance
from base_model.exchange_helpers.authenticator import Authenticator
from abc import ABC, abstractmethod

class Exchange(ABC):
    @abstractmethod
    def __init__(self, key, secret) -> None:
        ...
    

