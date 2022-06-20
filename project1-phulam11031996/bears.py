# int -> bool
def bears(n: int) -> bool:
    """Returns True if it's possible to get to 42.
    Returns False otherwise.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError

    if n == 42:
        return True

    if n < 42:
        return False

    if n % 2 == 0 and bears(n // 2):
        return True
    if n % 5 == 0 and bears(n - 42):
        return True

    prod_last_two = int(str(n)[-2]) * int(str(n)[-1])
    if n % 3 == 0 and prod_last_two != 0 and bears(n - prod_last_two):
        return True
    if n % 4 == 0 and prod_last_two != 0 and bears(n - prod_last_two):
        return True

    return False
