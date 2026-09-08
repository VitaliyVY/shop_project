import pytest

from src.users import UserRegistry


def test_create_and_find_user() -> None:
    registry = UserRegistry()
    user = registry.create_user("Olena Shevchenko", "olena@example.com")

    assert user.id == 1
    assert registry.find_by_email("OLENA@EXAMPLE.COM") == user


def test_display_name_uses_the_current_user_field() -> None:
    registry = UserRegistry()
    user = registry.create_user("Olena Shevchenko", "olena@example.com")

    assert registry.display_name(user) == "Olena Shevchenko"


def test_missing_user_raises_key_error() -> None:
    with pytest.raises(KeyError):
        UserRegistry().get_user(99)