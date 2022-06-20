from __future__ import annotations

from typing import Any, Optional


class Node:
    """Represents a node to be used in a doubly linked list."""
    def __init__(
            self,
            value: Any,
            prev: Optional[Node] = None,
            nxt: Optional[Node] = None):
        self.value = value

        # NOTE: This means that if prev and nxt are None, self.prev and
        # self.next will be self.  You may find this useful.  This means
        # that self.prev and self.next aren't Optional Nodes, they are
        # always Nodes.
        self.prev: Node = prev or self
        self.next: Node = nxt or self


class OrderedList:
    """A circular, doubly linked list of items, from lowest to highest.

    The contents of the list *must* have a accurate notation of less
    than and of equality.  That is to say, the contents of the list must
    implement both __lt__ and __eq__.
    """
    def __init__(self):
        self.head = Node(None, None, None)
        self.size = 0


# OrderedList, Any -> None
def insert(lst: OrderedList, value: Any) -> None:
    """Inserts the value into the proper location in the list.
    This function must have O(n) performance in the worst case.

    Args:
        lst: OrderedList
        value: int the value to be inserted

    Returns:
        None
    """
    temp = lst.head.next
    while (temp is not lst.head) and temp.value < value:
        temp = temp.next

    new_node = Node(value, temp.prev, temp)
    temp.prev.next = new_node
    temp.prev = new_node
    lst.size += 1


# OrderedList, Any -> None
def remove(lst: OrderedList, value: Any) -> None:
    """Removes the value from the list. If the value is not in the list,
    then this function should raise a ValueError.
    This function must have O(n) performance in the worst case.

    Args:
        lst: OrderedList
        value: int the value to be removed

    Returns:
            None

    Raises:
        ValueError if the value is not in the OrderedList
    """
    temp = lst.head
    while (temp.next is not lst.head) and temp.value != value:
        temp = temp.next
        if temp.value == value:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            lst.size -= 1
            return

    raise ValueError


# OrderedList, Value -> bool
def contains(lst: OrderedList, value: Any) -> bool:
    """Returns whether or not the valueis in the list.
    This function must have O(n) performance in the worst case.

    Args:
        lst: OrderedList
        value: int the value to be found

    Returns:
        bool
    """
    temp = lst.head.next
    while temp is not lst.head:
        if temp.value == value:
            return True
        temp = temp.next

    return False


# OrderedList, value -> int
def index(lst: OrderedList, value: Any) -> int:
    """Returns the index of the first occurrence of the value in the list.
    If the value is not in the list,
    then this function should raise a ValueError.
    This function must have O(n) performance in the worst case.

    Args:
        lst: OrderedList
        value: int the value to be found

    Returns:
        int

    Raises:
        ValueError if the value is not in the OrderedList
    """
    temp = lst.head.next
    index = 0
    while temp is not lst.head:
        if temp.value == value:
            return index
        index += 1
        temp = temp.next

    raise ValueError


# OrderedList, index -> Any
def get(lst: OrderedList, index: int) -> Any:
    """Returns the value at the given index. If the index is outside
    the bounds of the list, then this function should raise an IndexError.
    This function must have O(n) performance in the worst case.

    Args:
        lst: OrderedList
        index: int

    Returns:
        Any
    """
    if index < 0 or index >= lst.size:
        raise IndexError

    temp = lst.head
    for idx in range(index + 1):
        temp = temp.next

    return temp.value


# OrderedList, index -> Any
def pop(lst: OrderedList, index: int) -> Any:
    """Removes (and returns) the value at the given index.
    If the index is outside the bounds of the list,
    then this function should raise an IndexError.
    This function must have O(n) performance in the worst case.

    Args:
        lst: OrderedList
        index: int

    Returns:
        Any

    Raises:
        IndexError if the index is out of bound
    """
    if index < 0 or index >= lst.size:
        raise IndexError

    temp = lst.head
    for idx in range(index + 1):
        temp = temp.next

    temp.prev.next = temp.next
    temp.next.prev = temp.prev
    lst.size -= 1

    return temp.value


# OrderedList -> bool
def is_empty(lst: OrderedList) -> bool:
    """Returns whether or not the list is empty (Trueif it is,False otherwise).
    This function must have O(1) performance in the worst case.

    Args:
        lst: OrderedList

    Returns:
        bool
    """
    return lst.size == 0


# OrderedList -> int
def size(lst: OrderedList) -> int:
    """Returns the number of items in the list.
    This function must have O(1) performance in the worst case.

    Args:
        lst: OrderedList

    Returns:
        int
    """
    return lst.size
