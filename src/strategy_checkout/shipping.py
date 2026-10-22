from abc import ABC, abstractmethod

from .models import Order


class ShippingCostStrategy(ABC):
    """Contrato: cada estrategia sabe calcular el costo de envío de una orden."""

    @abstractmethod
    def calculate(self, order: Order) -> float:
        ...


class StandardShipping(ShippingCostStrategy):
    FREE_THRESHOLD = 1000.0
    FLAT_COST = 49.0

    def calculate(self, order: Order) -> float:
        if order.subtotal >= self.FREE_THRESHOLD:
            return 0.0
        return self.FLAT_COST


class ExpressShipping(ShippingCostStrategy):
    BASE = 99.0
    PER_KG = 12.0

    def calculate(self, order: Order) -> float:
        return self.BASE + self.PER_KG * order.weight_kg


class PickupShipping(ShippingCostStrategy):
    def calculate(self, order: Order) -> float:
        return 0.0


class SameDayShipping(ShippingCostStrategy):
    BASE = 149.0
    PER_KG = 18.0

    def calculate(self, order: Order) -> float:
        return self.BASE + self.PER_KG * order.weight_kg
