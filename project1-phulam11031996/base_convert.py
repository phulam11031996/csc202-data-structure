# int, int -> str
def convert(num: int, base: int) -> str:
    """Returns a string representing the number in the given base."""
    convert_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not isinstance(num, int):
        raise ValueError

    if base == 0:
        raise ZeroDivisionError

    if base <= 1 or base >= 37 or not isinstance(base, int):
        raise ValueError

    if num < base:
        return convert_string[num]

    return convert(num // base, base) + convert_string[num % base]
