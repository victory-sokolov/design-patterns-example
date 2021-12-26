from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def cancel_order(self):
        raise NotImplementedError

    @abstractmethod
    def verify_payment(self):
        raise NotImplementedError

    @abstractmethod
    def ship_order(self):
        raise NotImplementedError

class Order:
    def __init__(self):
        self.canceled_order_state = CanceledOrderState(self)
        self.payment_pending_state = PaymentPendingState(self)
        self.order_being_prepared_state = OrderBeingPreparedState(self)
        self.order_shipped_state = OrderShippedState(self)

        self.state = self.payment_pending_state
        self.current_state = self.state

    @property
    def state(self) -> State:
        return self.current_state

    @state.setter
    def state(self, state: State):
        self.current_state = state

class PaymentPendingState(State):
    def __init__(self, order: Order):
        self.order = order

    def cancel_order(self):
        print("Canceling your unpaid order...")
        self.order.state = self.order.canceled_order_state

    def verify_payment(self):
        print("Payment verified Shipping soon")
        self.order.state = self.order.order_being_prepared_state

    def ship_order(self):
        print("Cannot ship the order when payment is pending")

class CanceledOrderState(State):
    def __init__(self, order: Order):
        self.order = order

    def cancel_order(self):
        print("You order has already been canceled")

    def verify_payment(self):
        print("Order cancelled, you cannot verify payment.")

    def ship_order(self):
        print("Order cannot ship, it was cancelled")


class OrderBeingPreparedState(State):

    def __init__(self, order: Order):
        self.order = order

    def cancel_order(self):
        print("Canceling your order...")
        self.order.state = self.order.canceled_order_state

    def verify_payment(self):
        print("Already verified your payment.")

    def ship_order(self):
        print("Shipping your order now")
        self.order.state = self.order.order_shipped_state

class OrderShippedState(State):

    def __init__(self, order: Order):
        self.order = order

    def cancel_order(self):
        print("You cannot cancel, order alreayd shipped!")

    def verify_payment(self):
        print("You cannot verify payment, order already shipped")

    def ship_order(self):
        print("Already shipped")

order = Order()
order.state.verify_payment()
order.state.ship_order()
order.state.cancel_order()
print(f"Order state: {order.state}")
