"""Customer management operations."""

from .models import User


class UserRegistry:
    """In-memory registry of shop users."""

    def __init__(self) -> None:
        self._users: dict[int, User] = {}

    def create_user(self, full_name: str, email: str) -> User:
        """Create and register a user with the next available identifier."""
        user_id = max(self._users, default=0) + 1
        user = User(id=user_id, full_name=full_name, email=email)
        self._users[user_id] = user
        return user

    def get_user(self, user_id: int) -> User:
        """Return a user by identifier."""
        try:
            return self._users[user_id]
        except KeyError as error:
            raise KeyError(f"User {user_id} was not found") from error

    def find_by_email(self, email: str) -> User | None:
        """Find a user by an exact, case-insensitive email match."""
        normalized_email = email.casefold()
        return next(
            (user for user in self._users.values() if user.email.casefold() == normalized_email),
            None,
        )

    def display_name(self, user: User) -> str:
        """Return a short label for a user."""
        return user.name