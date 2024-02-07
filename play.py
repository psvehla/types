# play.py
"""Functions that return nothing."""

from typing import NoReturn


def play(player_name: str) -> None:
    """Play for the player."""
    print(f"{player_name} plays")


def black_hole() -> NoReturn:
    """Swallow execution path."""
    raise Exception("There is no going back...")


ret_val = play("Filip")
