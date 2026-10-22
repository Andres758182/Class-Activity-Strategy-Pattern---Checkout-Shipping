import pytest

from strategy_checkout.checkout import Checkout
from strategy_checkout.models import Order
from strategy_checkout.shipping import (
    ExpressShipping,
    PickupShipping,
    SameDayShipping,
    ShippingCostStrategy,
    StandardShipping,
)


# --- Standard ---

def test_standard_shipping_costs_49_below_threshold():
    assert Checkout(StandardShipping()).shipping_cost(Order(750.0, 2.0)) == 49.0


def test_standard_shipping_is_free_at_exactly_1000():
    assert Checkout(StandardShipping()).shipping_cost(Order(1000.0, 2.0)) == 0.0


def test_standard_shipping_is_free_above_1000():
    assert Checkout(StandardShipping()).shipping_cost(Order(1250.0, 3.5)) == 0.0


# --- Express ---

def test_express_shipping_uses_base_plus_weight():
    assert Checkout(ExpressShipping()).shipping_cost(Order(500.0, 3.5)) == 141.0


# --- Pickup ---

def test_pickup_is_free():
    assert Checkout(PickupShipping()).shipping_cost(Order(500.0, 3.5)) == 0.0


# --- Same Day (nueva) ---

def test_same_day_shipping_uses_149_plus_18_per_kg():
    # 149 + 18 * 3.5 = 212
    assert Checkout(SameDayShipping()).shipping_cost(Order(500.0, 3.5)) == 212.0


def test_same_day_with_zero_weight_is_just_the_base():
    assert Checkout(SameDayShipping()).shipping_cost(Order(500.0, 0.0)) == 149.0


# --- Checkout ---

def test_total_adds_shipping_cost():
    assert Checkout(StandardShipping()).total(Order(500.0, 2.0)) == 549.0


def test_total_with_same_day():
    # 500 + (149 + 18 * 2) = 685
    assert Checkout(SameDayShipping()).total(Order(500.0, 2.0)) == 685.0
    


def test_checkout_rejects_objects_that_are_not_strategies():
    with pytest.raises(TypeError):
        Checkout("teleport")


def test_strategy_contract_cannot_be_instantiated():
    with pytest.raises(TypeError):
        ShippingCostStrategy()


def test_checkout_works_with_any_new_strategy_without_changes():
    class FlatTenShipping(ShippingCostStrategy):
        def calculate(self, order):
            return 10.0

    assert Checkout(FlatTenShipping()).total(Order(100.0, 1.0)) == 110.0