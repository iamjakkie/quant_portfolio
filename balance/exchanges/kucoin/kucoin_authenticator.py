import time
import base64
import hmac
import hashlib

from base_model.authenticator import Authenticator

class KucoinAuthenticator(Authenticator):
    def __init__(self, api_key: str, api_secret: str, api_passphrase: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase

    def authenticate(self):
        now = int(time.time() * 1000)
        str_to_sign = str(now) + 'GET' + '/api/v1/accounts'
        signature = base64.b64encode(
            hmac.new(self.api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
        passphrase = base64.b64encode(hmac.new(self.api_secret.encode('utf-8'), self.api_passphrase.encode('utf-8'), hashlib.sha256).digest())
        headers = {
            "KC-API-SIGN": str(signature, 'utf-8'),
            "KC-API-TIMESTAMP": str(now),
            "KC-API-KEY": self.api_key,
            "KC-API-PASSPHRASE": str(passphrase, 'utf-8'),
            "KC-API-KEY-VERSION": "2"
        }
        return headers
