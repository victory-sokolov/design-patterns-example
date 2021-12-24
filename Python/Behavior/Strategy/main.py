from strategy import Order, ShippingCost
from strategy import FedExStrategy, PostalStrategy, UPSStrategy

# Test Federal Express shipping
order = Order()
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
assert cost == 3.0

# Test UPS shipping
order = Order()
strategy = UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

# Test Postal Service shipping
order = Order()
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0