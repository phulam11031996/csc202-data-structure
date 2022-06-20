from __future__ import annotations

from typing import List, Optional


# NOTE: This must be iterative, not recursive.  You should *not* modify
# the input list in any way.
def max_iterative(lst: Optional[list[float]]) -> Optional[float]:
    """Returns the maximum value in the given list.

    If the given list is empty, returns None.  If the given list is
    None, raises a ValueError.
    """
    if lst is None:
        raise ValueError

    if len(lst) == 0:
        return None

    max = lst[0]
    for val in lst:
        if val > max:
            max = val

    return max


# NOTE: This must be iterative, not recursive.  You should *not* modify
# the input list in any way, it will return a new list.
def reverse_list_iterative(lst: Optional[list[float]]) -> list[float]:
    """Reverses the given list.

    If the given list is None, raises a ValueError.
    """
    if lst is None:
        raise ValueError

    result = []
    for idx in range(len(lst) - 1, -1, -1):
        result.append(lst[idx])

    return result


# NOTE: This must be recursive, not iterative.  You should *not* modify
# the input list in any way, it will return a new list.
# NOTE: This will be inefficient, please never do this outside of this
# lab.
def reverse_list_recursive(lst: Optional[list[float]]) -> list[float]:
    """Reverses the given list.

    If the given list is None, raises a ValueError.
    """
    if lst is None:
        raise ValueError

    if len(lst) == 0:
        return []

    return [lst[-1]] + reverse_list_recursive(lst[:-1])
