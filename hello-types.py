# -*- coding: utf-8 -*-
"""Type hints."""


def headline(text, align=True):
    """Turn text into a headline."""
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")
