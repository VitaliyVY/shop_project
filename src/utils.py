"""General-purpose formatting and validation helpers."""

import re
from decimal import Decimal


def format_money(amount: Decimal) -> str:
    """Format a monetary amount with two decimal places."""
    return f"{amount:.2f} UAH"


def is_valid_email(email: str) -> bool:
    """Perform a small educational email-shape validation."""
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))