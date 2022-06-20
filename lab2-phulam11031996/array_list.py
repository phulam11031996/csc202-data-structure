from __future__ import annotations

from typing import Any, Optional


class ArrayList:
    def __init__(self, capacity: int = 1):
        self.list: list = [None] * capacity
        self.capacity: int = capacity
        self.size: int = 0


arr_list = Optional[ArrayList]


# no arguments -> list
def empty_list(capacity: int = 1) -> ArrayList:
    """Returns an empty list."""
    return ArrayList(capacity)


# ArrayList, int, Any -> ArrayList
def add(arr_list: ArrayList, index: int, value: Any) -> ArrayList:
    """Adds a value to an index position in the ArrayList"""
    # checks IndexError
    if index < 0 or index > arr_list.size:
        raise IndexError

    # resizes the list
    if arr_list.size >= arr_list.capacity:
        arr_list.capacity = arr_list.capacity * 2
        new_list = [None] * arr_list.capacity

        # copies to old list to new list
        for i in range(0, arr_list.size):
            new_list[i] = arr_list.list[i]

        arr_list.list = new_list

    # adds new value to the list
    for i in range(arr_list.size, index, -1):
        arr_list.list[i] = arr_list.list[i - 1]

    arr_list.size += 1
    arr_list.list[index] = value

    return arr_list


# ArrayList -> int
def length(arr_list: ArrayList) -> int:
    """Returns the number of elements currently in the list."""
    return arr_list.size


# ArrayList, int -> Any
def get(arr_list: ArrayList, index: int) -> Any:
    """Returns the value at the index positionin the list."""
    if index < 0 or index >= arr_list.size:
        raise IndexError

    return arr_list.list[index]


# ArrayList, int, value -> ArrayList
def setitem(arr_list: ArrayList, index: int, value: Any) -> ArrayList:
    """Returns the resulting list."""
    if index < 0 or index >= arr_list.size:
        raise IndexError

    arr_list.list[index] = value
    return arr_list


# ArrayList, int -> tuple
def remove(arr_list: ArrayList, index: int) -> tuple:
    """Returns a 2-tuple of, in this order, the element previously
    at the specified index and the resulting list."""
    if index < 0 or index >= arr_list.size:
        raise IndexError

    remove_value = arr_list.list[index]

    for i in range(index, arr_list.size - 1):
        arr_list.list[i] = arr_list.list[i + 1]

    arr_list.size -= 1

    for i in range(arr_list.size, arr_list.capacity):
        arr_list.list[i] = None

    return (remove_value, arr_list.list)
