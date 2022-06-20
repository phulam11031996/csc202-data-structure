from typing import Any


class CircularQueue:
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.cir_queue: list = [None] * self.capacity
        self.size: int = 0
        self.head: int = 0


# no arguments -> CircularQueue
def empty_queue() -> CircularQueue:
    """Returns an empty queue."""
    return CircularQueue()


# CircularQueue, Any -> None
def enqueue(queue: CircularQueue, value: Any) -> None:
    """No return"""
    if queue.size == queue.capacity:
        queue.capacity *= 2
        new_cir_queue = [None] * queue.capacity
        for index in range(queue.size):
            new_cir_queue[index] = queue.cir_queue[queue.head]
            queue.head = (queue.head + 1) % queue.size
        queue.head = 0
        queue.cir_queue = new_cir_queue

    cal_index = (queue.head + queue.size) % (queue.capacity)
    queue.cir_queue[cal_index] = value
    queue.size += 1


# CircularQueue -> Any
def dequeue(queue: CircularQueue) -> Any:
    """Returns the value at the “front” of the queue."""
    if is_empty(queue):
        raise IndexError

    dequeue_val = queue.cir_queue[queue.head]
    queue.cir_queue[queue.head] = None
    queue.head = (queue.head + 1) % queue.capacity
    queue.size -= 1

    return dequeue_val


# CircularQueue -> Any
def peek(queue: CircularQueue) -> Any:
    """Returns the value at the “front” of the queue."""
    if is_empty(queue):
        raise IndexError

    return queue.cir_queue[queue.head]


# CircullarQueue -> bool
def is_empty(queue: CircularQueue) -> bool:
    """Returns whether or not the queue is empty."""
    return queue.size == 0


# CircullarQueue -> int
def size(queue: CircularQueue) -> int:
    """Returns the number of items in the queue."""
    return queue.size
