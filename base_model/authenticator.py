from abc import ABC, abstractmethod

class Authenticator(ABC):

    @abstractmethod
    def authenticate():
        pass

    @abstractmethod
    def test():
        pass