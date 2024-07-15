from CEFI.binance.helpers.binance_authenticator import BinanceAuthenticator
from CEFI.binance.helpers.binance_connector import BinanceConnector
import os

def main():
    auth = BinanceAuthenticator(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_SECRET_KEY"))
    connector = BinanceConnector(auth)
    print(connector.get_account())

if __name__ == "__main__":
    main()