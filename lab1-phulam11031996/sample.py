from __future__ import annotations

from typing import Optional


def factorial(n: int) -> int:
    """Computes n! (that is, n factorial).

    If n is negative, raises a ValueError.
    """
    if n < 0:
        raise ValueError('factorial domain error')

    if n == 0:
        return 1

    return n * factorial(n - 1)


# NOTE: This code is remarkably inefficent, and you should never use it
# in practice.
def fibonacci(n: int) -> int:
    """Computes the n-th fibonacci number.

    If n is negative, raises a ValueError.
    """
    if n < 0:
        raise ValueError('fibonacci domain error')

    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# NOTE: This code is remarkably inefficent, and you should never use it
# in practice.
def max_recursive(lst: list[float]) -> Optional[float]:
    """Returns the maximum value in the given list.

    If the list is empty, returns None.
    """
    if len(lst) == 0:
        return None

    max_of_tail = max_recursive(lst[1:])

    if max_of_tail is None or lst[0] > max_of_tail:
        return lst[0]

    return max_of_tail


def reverse_string_iterative(string: str) -> str:
    """Reverses the given string."""
    result = []

    for i in range(len(string) - 1, -1, -1):
        result.append(string[i])

    return ''.join(result)
