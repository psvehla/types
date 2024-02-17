# choose.py
"""Any type example."""

import random
from typing import Any, Sequence


def choose(items: Sequence[Any]) -> Any:
    """Choose an item from the sequence."""
    return random.choice(items)


names = ["Guido", "Jukka", "Ivan"]
reveal_type(names)

name = choose(names)
reveal_type(name)
