from CEFI.binance.binance_client import BinanceClient
import os

def main():
    binance_client = BinanceClient(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_SECRET_KEY"))
    print(binance_client.get_balance())

if __name__ == "__main__":
    main()