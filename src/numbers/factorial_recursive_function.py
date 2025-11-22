from src.exceptions import NegativeNumberError


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise NegativeNumberError(n)
    elif n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)
