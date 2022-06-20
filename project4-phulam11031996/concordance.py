from __future__ import annotations

# Add more imports here as you use functions from your hash table.
from hash_table import HashTable, insert, contains, get_item, keys
import string


# str -> int
def djbx33a(s: str) -> int:
    """Returns a modified DJBX33A hash of the given string.

    See the project specification for the formula.
    """
    n = min(len(s), 8)
    summation = 0
    for i in range(n):
        summation += ord(s[i]) * pow(33, n - 1 - i)

    return 5381 * pow(33, n) + summation


# str -> HashTable
def build_stop_words_table(stop_words_filename: str) -> HashTable:
    """Returns a hash table whose keys are the stop words.

    This will read the stop words from the file and add them to the stop
    words table.  The values stored in the table will not matter.

    Args:
        stop_words_filename: the name of the stop words file.x

    Returns:
        A hash table whose keys are the stop words.
    """
    hash_table = HashTable(10, djbx33a)

    with open(stop_words_filename) as file:
        for line in file:
            insert(hash_table, line.strip(), None)

    return hash_table


# str HashTable -> HashTable
def build_concordance_table(filename: str, stop_table: HashTable) -> HashTable:
    """Returns the concordance table for the given file.

    This will read the given file and build a concordance table
    containing all valid words in the file.

    Args:
        filename: the name of the file to read
        stop_table: a hash table whose keys are the stop words

    Returns:
        A concordance table built from the given file.
    """
    hash_table = HashTable(10, djbx33a)

    with open(filename) as file:
        line_num = 1
        for line in file:

            fixed_line = ''
            for char in line:
                if char == "'":
                    continue
                elif char in string.punctuation:
                    fixed_line += ' '
                else:
                    fixed_line += char

            for word in fixed_line.lower().split():
                if word.isalpha() and not contains(stop_table, word):
                    if contains(hash_table, word):
                        line_nums = get_item(hash_table, word)
                        if line_nums[-1] != line_num:
                            line_nums.append(line_num)
                            insert(hash_table, word, line_nums)
                    else:
                        line_val = [line_num]
                        insert(hash_table, word, line_val)

            line_num += 1

    return hash_table


# str HashTable -> None
def write_concordance_table(
        filename: str, concordance_table: HashTable) -> None:
    """Writes the concordance table to the given file.

    This will sort the strings in the concordance table alphabetically
    and write them to the given file along with the line numbers on
    which they occurred.

    Args:
        filename: the name of the file in which to store the table
        concordance_table: the concordance table
    """
    key_words = keys(concordance_table)
    key_words.sort()
    line_nums = []

    for key in key_words:
        line_nums.append(get_item(concordance_table, key))

    with open(filename, 'w') as file:
        for idx in range(len(key_words)):
            file.write(key_words[idx] + ': ')
            file.write(' '.join(str(v) for v in line_nums[idx]))
            file.write('\n')
