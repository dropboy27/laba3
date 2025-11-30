import pytest
from src.math.factorial_function import factorial
from src.math.factorial_recursive_function import factorial_recursive
from src.math.fibo_function import fibo
from src.math.fibo_recursive_function import fibo_recursive
from src.exceptions import NegativeNumberError


@pytest.mark.parametrize("func", [factorial, factorial_recursive])
def test_factorial_valid(func):
    assert func(0) == 1
    assert func(1) == 1
    assert func(5) == 120


@pytest.mark.parametrize("func", [factorial, factorial_recursive])
def test_factorial_error(func):
    with pytest.raises(NegativeNumberError):
        func(-1)


@pytest.mark.parametrize("func", [fibo, fibo_recursive])
def test_fibo_valid(func):
    assert func(0) == 0
    assert func(1) == 1
    assert func(2) == 1
    assert func(6) == 8


@pytest.mark.parametrize("func", [fibo, fibo_recursive])
def test_fibo_error(func):
    with pytest.raises(NegativeNumberError):
        func(-5)
