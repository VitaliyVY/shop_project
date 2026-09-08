from decimal import Decimal

from src.models import Product
from src.orders import OrderManager
from src.payments import pay_order
from src.users import UserRegistry


def test_create_order_updates_stock_and_calculates_total() -> None:
    user = UserRegistry().create_user("Taras Bondar", "taras@example.com")
    product = Product(1, "Notebook", Decimal("80"), 10)
    order = OrderManager().create_order(1, user, [(product, 2)])

    assert product.quantity == 8
    assert order.total() == Decimal("160")


def test_order_discount_is_applied() -> None:
    user = UserRegistry().create_user("Taras Bondar", "taras@example.com")
    product = Product(1, "Notebook", Decimal("100"), 10)
    order = OrderManager().create_order(1, user, [(product, 2)])

    assert order.total(Decimal("10")) == Decimal("180")


def test_payment_marks_order_as_paid() -> None:
    user = UserRegistry().create_user("Taras Bondar", "taras@example.com")
    product = Product(1, "Notebook", 100, 10)
    order = OrderManager().create_order(1, user, [(product, 1)])

    assert pay_order(order, Decimal("100")) is True
    assert order.paid is True