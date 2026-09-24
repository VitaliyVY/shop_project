"""Command-line demonstration of the educational shop system."""

from decimal import Decimal

from src.models import Product
from src.orders import OrderManager
from src.products import ProductCatalog
from src.statistics import average_product_price, total_units_sold
from src.users import UserRegistry
from src.utils import format_money


def main() -> None:
    """Build a small catalog, place an order, and print a report."""
    catalog = ProductCatalog()
    catalog.add_product(Product(1, "Wireless headphones", Decimal("2500"), 8))
    catalog.add_product(Product(2, "USB cable", Decimal("300"), 20))

    users = UserRegistry()
    customer = users.create_user("Iryna Melnyk", "iryna@example.com")
    orders = OrderManager()
    order = orders.create_order(
        order_id=1,
        user=customer,
        requested_items=[
            (catalog.find_by_name("headphones")[0], 1),
            (catalog.find_by_name("cable")[0], 2),
        ],
    )

    print(f"Customer: {customer.full_name}")
    print(f"Order total: {format_money(order.total())}")
    average_price = format_money(average_product_price(catalog.all_products()))
    print(f"Average catalog price: {average_price}")
    print(f"Units sold: {total_units_sold(orders.all_orders())}")


if __name__ == "__main__":
    main()