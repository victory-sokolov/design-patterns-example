class ShippingCost:

    def __init__(self, strategy) -> None:
        self._strategy = strategy

    def shipping_cost(self, order):
        return self._strategy.calculate(order)