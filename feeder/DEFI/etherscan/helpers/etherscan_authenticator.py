from BASE_MODEL.authenticator import Authenticator

class EtherscanAuthenticator(Authenticator):
    def __init__(self, api_key: str):
        self.__api_key = api_key

    def authenticate(self, url:str):
        return f"{url}&apikey={self.__api_key}"