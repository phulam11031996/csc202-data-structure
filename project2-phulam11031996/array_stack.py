from typing import Any


class ArrayStack:
    def __init__(self, capacity: int = 5):
        self.items: list[Any] = [None] * capacity
        self.capacity: int = capacity
        self.size: int = 0


# no arguments -> ArrayStack
def empty_stack() -> ArrayStack:
    """Returns an empty stack."""
    return ArrayStack()


# ArrayStack, Any -> None
def push(stack: ArrayStack, value: Any) -> None:
    """No return"""
    if stack.size == stack.capacity:
        stack.capacity *= 2
        new_stack: list[Any] = [None] * stack.capacity

        for idx in range(len(stack.items)):
            new_stack[idx] = stack.items[idx]

        stack.items = new_stack

    stack.items[stack.size] = value
    stack.size += 1


# ArrayStack -> Any
def pop(stack: ArrayStack) -> Any:
    """Returns the element at the “top” of the stack."""
    if is_empty(stack):
        raise IndexError

    removed = stack.items[stack.size - 1]
    stack.items[stack.size - 1] = None
    stack.size -= 1

    return removed


# ArrayStack -> Any
def peek(stack: ArrayStack) -> Any:
    """Returns (without removing) the value on the “top” of thestack"""
    if is_empty(stack):
        raise IndexError

    return stack.items[stack.size - 1]


# ArrayStack -> bool
def is_empty(stack: ArrayStack) -> bool:
    """Returns whether or not the stack is empty."""
    return stack.size == 0


# ArrayStack -> int
def size(stack: ArrayStack) -> int:
    """Returns the number of items in the stack."""
    return stack.size
