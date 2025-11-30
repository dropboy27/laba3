from src.exceptions import NegativeNumberError


def factorial(n: int) -> int:
    if n < 0:
        raise NegativeNumberError(n)
    elif n == 0:
        return 1
    else:
        fac = 1
        for i in range(1, n+1):
            fac *= i
        return fac
