"""Simple payment simulation."""

from decimal import Decimal

from .models import Order


def pay_order(order: Order, amount: Decimal) -> bool:
    """Mark an order as paid when the supplied amount is sufficient."""
    if amount < order.total():
        return False
    order.paid = True
    return True