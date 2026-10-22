from .models import Order
from .shipping import ShippingCostStrategy


class Checkout:
    def __init__(self, shipping_strategy: ShippingCostStrategy):
        if not isinstance(shipping_strategy, ShippingCostStrategy):
            raise TypeError("shipping_strategy must be a ShippingCostStrategy")
        self.shipping_strategy = shipping_strategy

    def shipping_cost(self, order: Order) -> float:
        return self.shipping_strategy.calculate(order)

    def total(self, order: Order) -> float:
        return order.subtotal + self.shipping_cost(order)