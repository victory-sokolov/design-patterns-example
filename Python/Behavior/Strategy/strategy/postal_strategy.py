from abc_strategy import AbcStrategy

class PostalStrategy(AbcStrategy):
    def calculate(self, order):
        return 5.00