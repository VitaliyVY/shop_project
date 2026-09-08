"""Product catalog operations."""

from .models import Product


class ProductCatalog:
    """In-memory catalog supporting basic product management."""

    def __init__(self) -> None:
        self._products: dict[int, Product] = {}

    def add_product(self, product: Product) -> None:
        """Add a product, rejecting duplicate identifiers."""
        if product.id in self._products:
            raise ValueError(f"Product {product.id} already exists")
        self._products[product.id] = product

    def remove_product(self, product_id: int) -> Product:
        """Remove and return a product by identifier."""
        try:
            return self._products.pop(product_id)
        except KeyError as error:
            raise KeyError(f"Product {product_id} was not found") from error

    def find_by_name(self, query: str) -> list[Product]:
        """Find products whose names contain ``query`` case-insensitively."""
        normalized_query = query.casefold()
        return [
            product
            for product in self._products.values()
            if normalized_query in product.name.casefold()
        ]

    def all_products(self) -> list[Product]:
        """Return all products in insertion order."""
        return list(self._products.values())