from decimal import Decimal

import pytest

from src.models import Product
from src.products import ProductCatalog


def test_catalog_add_search_and_remove() -> None:
    catalog = ProductCatalog()
    catalog.add_product(Product(1, "Keyboard", Decimal("1200"), 5))
    catalog.add_product(Product(2, "Mouse", Decimal("500"), 3))

    assert [product.name for product in catalog.find_by_name("KEY")] == ["Keyboard"]
    assert catalog.remove_product(2).name == "Mouse"


def test_catalog_rejects_duplicate_product_ids() -> None:
    catalog = ProductCatalog()
    catalog.add_product(Product(1, "Keyboard", 1200, 5))

    with pytest.raises(ValueError):
        catalog.add_product(Product(1, "Another keyboard", 900, 2))