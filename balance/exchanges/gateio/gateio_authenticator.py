import time
import hashlib
import hmac

from base_model.authenticator import Authenticator

class GateioAuthenticator(Authenticator):
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key
        self.headers = {}

    def authenticate(self):
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        url = '/api/v4/spot/accounts'
        t = time.time()
        m = hashlib.sha512()
        m.update(("").encode('utf-8'))
        hashed_payload = m.hexdigest()
        query_param = ''
        method = 'GET'
        s = '%s\n%s\n%s\n%s\n%s' % (method, url, "", hashed_payload, t)
        sign = hmac.new(self.secret_key.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
        sign_headers = {'KEY': self.api_key, 'Timestamp': str(t), 'SIGN': sign}
        headers.update(sign_headers)
        return headers
        