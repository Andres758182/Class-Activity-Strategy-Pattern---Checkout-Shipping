import pytest
from strategy_checkout.checkout import Checkout
from strategy_checkout.models import Order

def test_standard_shipping_costs_49_below_threshold():
    assert Checkout().shipping_cost(Order(750.0, 2.0), "standard") == 49.0

def test_standard_shipping_is_free_at_1000_or_more():
    assert Checkout().shipping_cost(Order(1250.0, 3.5), "standard") == 0.0

def test_express_shipping_uses_base_plus_weight():
    assert Checkout().shipping_cost(Order(500.0, 3.5), "express") == 141.0

def test_pickup_is_free():
    assert Checkout().shipping_cost(Order(500.0, 3.5), "pickup") == 0.0

def test_total_adds_shipping_cost():
    assert Checkout().total(Order(500.0, 2.0), "standard") == 549.0

def test_unknown_service_is_rejected():
    with pytest.raises(ValueError):
        Checkout().shipping_cost(Order(500.0, 2.0), "teleport")
