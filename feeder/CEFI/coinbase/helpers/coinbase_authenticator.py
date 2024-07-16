from BASE_MODEL.authenticator import Authenticator

import jwt
from cryptography.hazmat.primitives import serialization
import time
import secrets

class CoinbaseAuthenticator(Authenticator):
    def __init__(self, key_name: str, key_secret: str):
        self.__key_name = key_name
        self.__key_secret = key_secret

    def authenticate(self, uri:str):
        private_key_bytes = self.__key_secret.encode('utf-8')
        private_key = serialization.load_pem_private_key(private_key_bytes, password=None)
        jwt_payload = {
            'sub': self.__key_name,
            'iss': 'cdp',
            'nbf': int(time.time()),
            'exp': int(time.time()) + 120,
            'uri': uri,
        }
        jwt_token = jwt.encode(
            jwt_payload,
            private_key,
            algorithm='ES256',
            headers={'kid': self.__key_name, 'nonce': secrets.token_hex()},
        )
        return jwt_token
        