from __future__ import annotations

from typing import Any, Optional


class Node:
    def __init__(self, value: Any, nxt: Optional[Node] = None):
        self.value = value
        self.next = nxt

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Node) and
            other.value == self.value and
            other.next == self.next
        )


class LinkedQueue:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0


# no arguments -> LinkedQueue
def empty_queue() -> LinkedQueue:
    """Returns an empty queue."""
    return LinkedQueue()


# LinkedQueue, value -> None
def enqueue(queue: LinkedQueue, value: Any) -> None:
    """No return"""
    if queue.tail is None:
        queue.head = Node(value, None)
        queue.tail = queue.head
    else:
        queue.tail.next = Node(value, None)
        queue.tail = queue.tail.next

    queue.size += 1


# LinkedQueue -> Any
def dequeue(queue: LinkedQueue) -> Any:
    """Returns the value at the “front” of the queue.

    Raise IndexError if the queue is empty"""
    if queue.head == queue.tail is None:
        raise IndexError

    removed = queue.head.value
    queue.head = queue.head.next
    queue.size -= 1

    if size(queue) == 0:
        queue.head = None
        queue.tail = None

    return removed


# LinkedQueue -> Any
def peek(queue: LinkedQueue) -> Any:
    """Returns the value at the “front” of the queue"""
    if is_empty(queue):
        raise IndexError

    return queue.head.value


# LinkedQueue -> bool
def is_empty(queue: LinkedQueue) -> bool:
    """Return True if the Queue is empty"""
    return queue.head == queue.tail is None


# LinkedQueue -> int
def size(queue: LinkedQueue) -> int:
    """Returns the number of items in the queue"""
    if is_empty(queue):
        return 0

    return queue.size
