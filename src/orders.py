"""Order creation and inventory operations."""

from .models import Order, OrderItem, Product, User


class OrderManager:
    """Create orders while reserving product quantities."""

    def __init__(self) -> None:
        self._orders: dict[int, Order] = {}

    def create_order(
        self, order_id: int, user: User, requested_items: list[tuple[Product, int]]
    ) -> Order:
        """Create an order and decrease inventory for each requested item."""
        if order_id in self._orders:
            raise ValueError(f"Order {order_id} already exists")
        if not requested_items:
            raise ValueError("An order must contain at least one item")

        items: list[OrderItem] = []
        for product, quantity in requested_items:
            if quantity <= 0:
                raise ValueError("Order quantity must be positive")
            if product.quantity < quantity:
                raise ValueError(f"Not enough stock for {product.name}")
            product.quantity -= quantity
            items.append(OrderItem(product=product, quantity=quantity))

        order = Order(id=order_id, user=user, items=items)
        self._orders[order_id] = order
        return order

    def get_order(self, order_id: int) -> Order:
        """Return an order by identifier."""
        return self._orders[order_id]

    def all_orders(self) -> list[Order]:
        """Return all created orders."""
        return list(self._orders.values())