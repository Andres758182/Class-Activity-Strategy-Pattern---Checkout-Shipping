from dataclasses import dataclass

@dataclass(frozen=True)
class Order:
    subtotal: float
    weight_kg: float
