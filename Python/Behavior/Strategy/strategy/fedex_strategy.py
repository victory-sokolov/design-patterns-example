from abc_strategy import AbcStrategy

class FedExStrategy(AbcStrategy):
    def calculate(self, order):
        return 3.00