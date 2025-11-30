import pytest
from src.stack_class import Stack
from src.exceptions import EmptyStackError


@pytest.fixture
def stack():
    """Фикстура создает пустой стек для каждого теста."""
    return Stack()


def test_push_and_peek(stack):
    stack.push(10)
    assert stack.peek() == 10
    assert len(stack) == 1

    stack.push(20)
    assert stack.peek() == 20
    assert len(stack) == 2


def test_pop(stack):
    stack.push(10)
    stack.push(20)

    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.is_empty() is True


def test_empty_stack_errors(stack):
    assert stack.is_empty() is True

    with pytest.raises(EmptyStackError):
        stack.pop()

    with pytest.raises(EmptyStackError):
        stack.peek()


def test_min_stack_feature(stack):
    stack.push(5)
    stack.push(3)
    stack.push(7)

    assert stack.pop() == 7
    assert stack.pop() == 3
    assert stack.pop() == 5


def test_stack_min():
    s = Stack()
    s.push(5)
    assert s.min() == 5

    s.push(3)
    assert s.min() == 3

    s.push(7)
    assert s.min() == 3

    s.push(1)
    assert s.min() == 1

    s.pop()
    assert s.min() == 3

    s.pop()
    assert s.min() == 3

    s.pop()
    assert s.min() == 5


def test_stack_min_empty():
    s = Stack()
    with pytest.raises(EmptyStackError):
        s.min()
