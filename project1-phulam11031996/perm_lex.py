from __future__ import annotations


# string -> list[str]
def perm_gen_lex(string: str) -> list[str]:
    """Return a list of all permutations of the characters
    in s in the lexicographic order."""
    if not isinstance(string, str):
        raise ValueError

    if len(string) == 0:
        return ['']

    if len(string) == 1:
        return [string]

    result = []
    for char in string:
        temp = string.replace(char, '')
        permutations = perm_gen_lex(temp)
        for per in permutations:
            result.append(char + per)

    return result
