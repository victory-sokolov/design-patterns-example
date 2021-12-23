from abc import ABC, abstractmethod
from typing import List

class Exchange(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_market_data(self, coin: str) -> List[float]:
        pass

class BinanceExchange(Exchange):
    def connect(self):
        print("Connecting to Binance")

    def get_market_data(self, coin: str) -> List[float]:
        return [10,12,18,22]


class CoinBase(Exchange):

    def connect(self):
        print("Connecting to Binance")

    def get_market_data(self, coin: str) -> List[float]:
        return [11,13,17,21]


class TradingBot(ABC):

    def __init__(self, exchange: Exchange):
        self.exchange = exchange

    @abstractmethod
    def should_buy(self, prices) -> bool:
        pass

    @abstractmethod
    def should_sell(self, prices) -> bool:
        pass

    def check_prices(self, coin: str):
        self.exchange.connect()
        prices = self.exchange.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}")
        elif should_sell:
            print(f"You should sell {coin}")

class AverageTrader(TradingBot):

    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices) -> bool:
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices) -> bool:
        return prices[-1] > self.list_average(prices)


class MinMaxTrader(TradingBot):

    def should_buy(self, prices) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices) -> bool:
        return prices[-1] == max(prices)


minmax = AverageTrader(CoinBase())
minmax.check_prices("BTC")
