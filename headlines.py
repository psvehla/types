# -*- coding: utf-8 -*-
# headlines.py
"""Type hints."""


def headline(text: str, align: bool = True) -> str:
    """Turn text into a headline."""
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


print(headline("python type checking"))
print()
print(headline("python type checking", align=False))
print()
print(headline("use mypy", align=True))
