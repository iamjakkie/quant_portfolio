from BASE_MODEL.authenticator import Authenticator

import time
import hashlib
import hmac

class GateIOAuthenticator(Authenticator):
    def __init__(self, api_key:str, api_secret:str):
        self.__api_key = api_key
        self.__api_secret = api_secret

    def authenticate(self, uri:str):
        t = time.time()
        m = hashlib.sha512()
        # m.update("").encode('utf-8')
        hashed_payload = m.hexdigest()
        s = f"GET\n{uri}\n\n{hashed_payload}\n{t}"
        signature = hmac.new(self.__api_secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
        return {
            "KEY": self.__api_key,
            "Timestamp": str(t),
            "SIGN": signature
        }