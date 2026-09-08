"""Core data models for the shop application."""

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class Product:
    """A product available in the shop."""

    id: int
    name: str
    price: Decimal
    quantity: int

    def __post_init__(self) -> None:
        """Normalize prices and validate basic product data."""
        self.price = Decimal(str(self.price))
        if self.price < 0:
            raise ValueError("Product price cannot be negative")
        if self.quantity < 0:
            raise ValueError("Product quantity cannot be negative")


@dataclass
class User:
    """A customer registered in the shop."""

    id: int
    full_name: str
    email: str


@dataclass
class OrderItem:
    """A product and the quantity bought in one order."""

    product: Product
    quantity: int

    @property
    def subtotal(self) -> Decimal:
        """Return the cost of this order line."""
        return self.product.price * self.quantity


@dataclass
class Order:
    """A collection of products purchased by one user."""

    id: int
    user: User
    items: list[OrderItem] = field(default_factory=list)
    paid: bool = False

    def total(self, discount: Decimal = Decimal("0")) -> Decimal:
        """Return the order total after a percentage discount.

        ``discount`` is expressed as a percentage from 0 to 100.
        """
        subtotal = sum((item.subtotal for item in self.items), Decimal("0"))
        if not 0 <= discount <= 100:
            raise ValueError("Discount must be between 0 and 100")
        discounted_total = subtotal * (Decimal("1") - discount / Decimal("100"))
        return subtotal