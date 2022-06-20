from __future__ import annotations

from typing import Optional

from ordered_list import (
    OrderedList, insert, pop
)


class HuffmanNode:
    """Represents a node in a Huffman tree.

    Attributes:
        char: The character as an integer ASCII value
        frequency: The frequency of the character in the file
        left: The left Huffman sub-tree
        right: The right Huffman sub-tree
    """
    def __init__(
            self,
            char: int,
            frequency: int,
            left: Optional[HuffmanNode] = None,
            right: Optional[HuffmanNode] = None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        """Returns True if and only if self and other are equal."""
        return (
            isinstance(other, HuffmanNode) and
            self.frequency == other.frequency and
            self.char == other.char and
            self.left == other.left and
            self.right == other.right
        )

    def __lt__(self, other) -> bool:
        """Returns True if and only if self < other."""
        if self.frequency == other.frequency:
            return self.char < other.char

        return self.frequency < other.frequency


# ############################# PROJECT 3A BEGINS ########################### #
# str -> list[int]
def count_frequencies(filename: str) -> list[int]:
    """Reads the given file and counts the frequency of each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the frequency with which that character occured.
    """
    char_freq = [0] * 256
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                char_freq[ord(char)] += 1

    return char_freq


# list[int] -> Optional[HuffmanNode]
def build_huffman_tree(frequencies: list[int]) -> Optional[HuffmanNode]:
    """Creates a Huffman tree of the characters with non-zero frequency.

    Returns the root of the tree.
    """
    if frequencies == ([0] * 256):
        return None

    ordered_list = OrderedList()
    for idx, fre in zip(range(len(frequencies)), frequencies):
        if fre != 0:
            huffman_node = HuffmanNode(idx, fre)
            insert(ordered_list, huffman_node)

    while ordered_list.size > 1:
        left = pop(ordered_list, 0)
        right = pop(ordered_list, 0)
        sum_fre = left.frequency + right.frequency

        if left.char < right.char:
            huffman_tree = HuffmanNode(left.char, sum_fre, left, right)
        else:
            huffman_tree = HuffmanNode(right.char, sum_fre, left, right)

        insert(ordered_list, huffman_tree)

    return ordered_list.head.next.value


# Optional[HuffmanNode] -> list[str]
def create_codes(tree: Optional[HuffmanNode], arr=[], track='') -> list[str]:
    """Traverses the tree creating the Huffman code for each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the Huffman code for that character.
    """
    if arr == []:
        arr = [''] * 256

    if tree is None:
        return arr

    if tree.left is None and tree.right is None:
        arr[tree.char] = track

    create_codes(tree.right, arr, track + '1')
    create_codes(tree.left, arr, track + '0')

    return arr


# list[int] -> str
def create_header(frequencies: list[int]) -> str:
    """Returns the header for the compressed Huffman data.

    For example, given the file "aaaccbbbb", this would return:
    "97 3 98 4 99 2"
    """
    temp_list = []

    for idx in range(len(frequencies)):
        if frequencies[idx] != 0:
            temp_list.append(str(idx))
            temp_list.append(str(frequencies[idx]))

    return ' '.join(temp_list)


# str str -> None
def huffman_encode(in_filename: str, out_filename: str) -> None:
    """Encodes the data in the input file, writing the result to the
    output file."""
    file_string = ''
    with open(in_filename, 'r') as file:
        for line in file:
            for char in line:
                file_string += char

    freq_list = count_frequencies(in_filename)
    huffman_tree = build_huffman_tree(freq_list)
    code_list = create_codes(huffman_tree)
    header_str = create_header(freq_list)

    with open(out_filename, 'w') as file:
        file.write(header_str)
        file.write('\n')
        for char in file_string:
            file.write(code_list[ord(char)])


# ############################# PROJECT 3B BEGINS ########################### #
# str -> list[int]
def parse_header(ascii_freg: str) -> list[int]:
    frequencies = [0] * 256
    lst_fre = ascii_freg.split()

    for idx in range(len(lst_fre)):
        if idx % 2 == 0:
            frequencies[int(lst_fre[idx])] = int(lst_fre[idx + 1])

    return frequencies


# str str -> None
def huffman_decode(in_filename: str, out_filename: str) -> None:
    with open(in_filename, 'r') as file:
        ascii_fre = file.readline()
        codes = file.readline()

    if ascii_fre == '\n':  # file is empty
        with open(out_filename, 'w'):
            return

    if codes == '':  # file with no code
        with open(out_filename, 'w') as file:
            temp_codes = ascii_fre.split()
            for c in range(int(temp_codes[1])):
                file.write(chr(int(temp_codes[0])))
        return

    frequencies = parse_header(ascii_fre)  # create tree
    huffman_tree = build_huffman_tree(frequencies)

    with open(out_filename, 'w') as file:  # normal case
        temp = huffman_tree
        for code in codes:
            if code == '0':
                temp = temp.left
                if temp.left is None and temp.right is None:
                    file.write(chr(temp.char))
                    temp = huffman_tree
            else:  # code == '1':
                temp = temp.right
                if temp.left is None and temp.right is None:
                    file.write(chr(temp.char))
                    temp = huffman_tree
        return
