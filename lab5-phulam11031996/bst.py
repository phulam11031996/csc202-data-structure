from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Optional


class TreeNode:
    def __init__(
            self,
            value: Any = None,
            left: Optional[TreeNode] = None,
            right: Optional[TreeNode] = None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (
            isinstance(other, TreeNode) and
            self.left == other.left and
            self.right == other.right
        )

    def __repr__(self):
        return '{}({}, {}, {})'.format(
                    self.__class__.__name__,
                    repr(self.value),
                    repr(self.left) if self.left else None,
                    repr(self.right) if self.right else None) \
                        .replace(', None, None)', ')') \
                        .replace(', None)', ')')


BST = Optional[TreeNode]


def is_empty(tree: BST) -> bool:
    return tree is None


def search(tree: BST, value: Any) -> bool:
    if tree is None:
        return False

    return (
        tree.value == value or
        search(tree.left, value) or
        search(tree.right, value)
    )


def insert(tree: BST, value: Any) -> BST:
    if tree is None:
        return TreeNode(value)

    if tree.value > value:
        tree.left = insert(tree.left, value)
    else:   # tree.value <= value:
        tree.right = insert(tree.right, value)

    return tree


def delete(tree: BST, value: Any) -> BST:

    if tree is None:    # value not found returns the original list
        return None

    if tree.value > value:
        tree.left = delete(tree.left, value)
    elif tree.value < value:
        tree.right = delete(tree.right, value)
    else:
        if tree.right is None:
            return tree.left
        elif tree.left is None:
            return tree.right
        else:
            max_val = find_min(tree.right)
            tree.value = max_val
            tree.right = delete(tree.right, max_val)
      
    return tree


def find_min(tree: BST) -> Any:
    if is_empty(tree):
        raise ValueError

    while tree.left:
        tree = tree.left

    return tree.value


def find_max(tree: BST) -> Any:
    if is_empty(tree):
        raise ValueError

    while tree.right:
        tree = tree.right

    return tree.value


def height(tree: BST) -> int:
    if is_empty(tree):
        return -1

    return max(1 + height(tree.right), 1 + height(tree.left))


def prefix_iterator(tree: BST) -> Iterator[Any]:
    if tree:
        yield tree.value
        yield from prefix_iterator(tree.left)
        yield from prefix_iterator(tree.right)


def infix_iterator(tree: BST) -> Iterator[Any]:
    if tree:
        yield from infix_iterator(tree.left)
        yield tree.value
        yield from infix_iterator(tree.right)


def postfix_iterator(tree: BST) -> Iterator[Any]:
    if tree:
        yield from postfix_iterator(tree.left)
        yield from postfix_iterator(tree.right)
        yield tree.value
