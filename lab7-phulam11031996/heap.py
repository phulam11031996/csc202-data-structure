# NOTE: Do not import anything else.
from __future__ import annotations

from typing import Any


class MaxHeap:
    def __init__(self):
        self.items = [None]


# MaxHeap -> None
def perc_up(heap: MaxHeap, size: int) -> None:
    """

    """
    while size // 2 > 0:
        if heap.items[size] > heap.items[size // 2]:
            heap.items[size], heap.items[size // 2] = \
                heap.items[size // 2], heap.items[size]
        size = size // 2


# MaxHeap, Any -> None
def enqueue(heap: MaxHeap, item: Any) -> None:
    """

    """
    heap.items.append(item)
    perc_up(heap, len(heap.items) - 1)


# MaxHeap Any -> None
def perc_down(heap: MaxHeap, i: Any) -> None:
    """

    """
    while (i * 2) <= len(heap.items) - 1:
        mc_idx = max_child(heap, i)
        if heap.items[i] < heap.items[mc_idx]:
            heap.items[i], heap.items[mc_idx] = \
                heap.items[mc_idx], heap.items[i]
        i = mc_idx


# MaxHeap i -> None
def max_child(heap: MaxHeap, i: Any) -> None:
    """

    """
    if i * 2 + 1 > len(heap.items) - 1:
        return i * 2
    else:
        if heap.items[i * 2] > heap.items[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1


# MaxHeap -> Any
def dequeue(heap: MaxHeap) -> Any:
    """

    """
    if size(heap) == 0:
        raise IndexError

    deq_val = heap.items[1]
    heap.items[1] = heap.items[len(heap.items) - 1]
    heap.items.pop()
    perc_down(heap, 1)
    return deq_val


# MaxHeap -> Any
def peek(heap: MaxHeap) -> Any:
    """

    """
    if len(heap.items) == 1:
        raise IndexError

    return heap.items[1]


# MaxHeap -> Any
def size(heap: MaxHeap) -> Any:
    """

    """
    return len(heap.items) - 1


# NOTE: To be used for testing
def _contents(heap: MaxHeap) -> list[Any]:
    """

    """
    return heap.items[1:]


# list[Any] -> MaxHeap
def heapify(lst: list[Any]) -> MaxHeap:
    """

    """
    heap = MaxHeap()
    heap.items = [None] + lst[:]

    i = len(lst) // 2
    while (i > 0):
        perc_down(heap, i)
        i = i - 1

    return heap


# list[Any] -> None
def heap_sort(lst: list[Any]) -> None:
    """

    """
    heap = heapify(lst)
    for i in range(len(lst) - 1, -1, -1):
        lst[i] = dequeue(heap)
