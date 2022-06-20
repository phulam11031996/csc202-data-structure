from __future__ import annotations

from collections.abc import Callable, Hashable
from typing import Any, List, Tuple


# An entry in the hash table is a key-value pair
HashEntry = Tuple[Hashable, Any]
# Each entry in the hash table array will be a list of HashEntry pairs
HashChain = List[HashEntry]


class HashTable:
    """A hash table with separate chaining."""
    def __init__(
            self,
            capacity: int = 10,
            hash_function: Callable[[Hashable], int] = hash):
        """Creates an empty hash table.

        Args:
            capacity:
                The initial capacity of the backing array.  The default
                capacity is 10.
            hash_function:
                The function to use to compute hash values for the given
                keys.  The default hash function is the Python builtin
                hash function.
        """
        self.table: list[HashChain] = [[] for _ in range(capacity)]

        self.size: int = 0
        self.capacity: int = capacity
        self.hash_function = hash_function


# NOTE: Computing the hash value of the key could be slow, we should
# only do it once.
# HashTable Hashable Any -> None
def insert(hash_table: HashTable, key: Hashable, value: Any) -> None:
    hash_key = hash_table.hash_function(key) % hash_table.capacity
    for idx in range(len(hash_table.table[hash_key])):
        if hash_table.table[hash_key][idx][0] == key:
            hash_table.table[hash_key][idx] = (key, value)
            return

    if load_factor(hash_table) >= 1:
        hash_table.capacity *= 2
        new_table: list[HashChain] = [[] for _ in range(hash_table.capacity)]

        for hash_chain in hash_table.table:
            for pair in hash_chain:
                hash_value = hash_table.hash_function(pair[0])
                new_table[hash_value % hash_table.capacity].append(pair)

        hash_table.table = new_table

    hash_key = hash_table.hash_function(key) % hash_table.capacity
    hash_table.table[hash_key].append((key, value))
    hash_table.size += 1


# HashTable, Hashable -> Any
def get_item(hash_table: HashTable, key: Hashable) -> Any:
    pos = hash_table.hash_function(key) % hash_table.capacity

    for pair in hash_table.table[pos]:
        if pair[0] == key:
            return pair[1]

    raise KeyError


# HashTable, Hashable -> bool
def contains(hash_table: HashTable, key: Hashable) -> bool:
    pos = hash_table.hash_function(key) % hash_table.capacity

    for entry in hash_table.table[pos]:
        if entry[0] == key:
            return True

    return False


# HashTable Hahsable -> tuple[Hashable, Any]
def remove(hash_table: HashTable, key: Hashable) -> tuple[Hashable, Any]:
    pos = hash_table.hash_function(key) % hash_table.capacity

    for idx in range(len(hash_table.table[pos])):
        if hash_table.table[pos][idx][0] == key:
            hash_table.size -= 1
            return hash_table.table[pos].pop(idx)

    raise KeyError


# HashTable -> int
def size(hash_table: HashTable) -> int:
    return hash_table.size


# HashTable -> list[Hashable]
def keys(hash_table: HashTable) -> list[Hashable]:
    lst = []
    for hash_chain in hash_table.table:
        for pair in hash_chain:
            lst.append(pair[0])

    return lst


# HashTable -> float
def load_factor(hash_table: HashTable) -> float:
    return hash_table.size / hash_table.capacity


# HashTable -> list[HashChain]
def _contents(hash_table: HashTable) -> list[HashChain]:
    return hash_table.table
