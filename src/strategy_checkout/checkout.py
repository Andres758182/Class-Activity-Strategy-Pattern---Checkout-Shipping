from .models import Order

class Checkout:
    def shipping_cost(self, order: Order, service: str) -> float:
        if service == "standard":
            if order.subtotal >= 1000:
                return 0.0
            return 49.0

        if service == "express":
            return 99.0 + 12.0 * order.weight_kg

        if service == "pickup":
            return 0.0

        raise ValueError(f"Unsupported service: {service}")

    def total(self, order: Order, service: str) -> float:
        return order.subtotal + self.shipping_cost(order, service)
