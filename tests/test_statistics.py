from decimal import Decimal

import pytest

from src.models import Product
from src.statistics import average_product_price, total_units_sold


def test_average_product_price() -> None:
    products = [Product(1, "A", 10, 1), Product(2, "B", 20, 1)]

    assert average_product_price(products) == Decimal("15")


def test_average_price_of_empty_catalog_is_zero() -> None:
    assert average_product_price([]) == Decimal("0")


def test_total_units_sold_for_no_orders_is_zero() -> None:
    assert total_units_sold([]) == 0