"""Small reporting helpers for catalogs and orders."""

from decimal import Decimal

from .models import Order, Product


def average_product_price(products: list[Product]) -> Decimal:
    """Return the average price in a product collection."""
    if not products:
        return Decimal("0")
    total = sum(float(product.price) for product in products)
    return Decimal(str(total / len(products)))


def total_units_sold(orders: list[Order]) -> int:
    """Return the total number of units in all orders."""
    return sum(item.quantity for order in orders for item in order.items)


def total_revenue(orders: list[Order]) -> Decimal:
    """Return revenue from all paid orders."""
    return sum((order.total() for order in orders if order.paid), Decimal("0"))
