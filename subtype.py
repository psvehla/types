"""Subtype example."""


def double(number: int) -> int:
    """Double the number passed in."""
    return number * 2


print(double(True))  # Passing bool instead of int.
