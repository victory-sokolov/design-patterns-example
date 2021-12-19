import time

class Producer:
    """Define the resource-intensive object to instantiate"""
    def produce(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy:
    """Define the relatively less resource-intensive proxy to instantiate a middleman"""
    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        """Check if producer is available"""
        if self.occupied == "No":
            # if producer is availabe, create a producer object
            self.producer = Producer()
            # Make producer meet the guest
            self.producer.meet()
        else:
            # don't instantiate producer
            time.sleep(2)
            print("Producer is busy")


proxy = Proxy()
proxy.produce()
# Change state to occupied
proxy.occupied = "Yes"
proxy.produce()


class CryptoCurrencyApi:
    crypto = [
        {
            'currency' : 'Bitcoin',
            'price': '$8.500'
        },
        {
            'currency' : 'Litecoin',
            'price': '$50'
        },
        {
            'currency' : 'Ethereum',
            'price': '$1.500'
        }
    ]

    def get_coin(self, coin):
        for currency in self.crypto:
            if currency['currency'] == coin:
                return currency


class CryptoCUrrencyProxy:

    def __init__(self):
        self.api = CryptoCurrencyApi()
        self.cache = {}

    def get_coin(self, coin: str):
        if not self.cache.get(coin):
            self.cache[coin] = self.api.get_coin(coin)

        return self.cache[coin]

crypto = CryptoCUrrencyProxy()
res = crypto.get_coin("Bitcoin")
print(res)
