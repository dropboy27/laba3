import typer
from typing import List, Optional
from src.sortings.quick_sort_function import quick_sort
from src.sortings.bubble_sort_function import bubble_sort
from src.sortings.heap_sort_function import heap_sort
from src.sortings.counting_sort_function import counting_sort
from src.sortings.radix_sort_function import radix_sort
from src.sortings.bucket_sort_function import bucket_sort
from src.math.factorial_function import factorial
from src.math.factorial_recursive_function import factorial_recursive
from src.math.fibo_function import fibo
from src.math.fibo_recursive_function import fibo_recursive
from src.stack_class import Stack

app = typer.Typer()


@app.command()
def sort(
    numbers: List[int],
    algo: str = typer.Option("quick", help="Алгоритм сортировки")
):
    """Сортировка массива чисел"""
    algorithms = {
        "quick": quick_sort,
        "bubble": bubble_sort,
        "counting": counting_sort,
        "radix": radix_sort,
    }

    if algo == "heap":
        arr = numbers.copy()
        heap_sort(arr)
        result = arr
    elif algo in algorithms:
        result = algorithms[algo](numbers)
    else:
        typer.echo(f"Неизвестный алгоритм: {algo}")
        typer.echo(
            f"Доступны: {', '.join(list(algorithms.keys()) + ['heap'])}")
        raise typer.Exit(1)

    typer.echo(f"Входные данные: {numbers}")
    typer.echo(f"Результат ({algo}): {result}")


@app.command()
def fact(
    n: int,
    recursive: bool = typer.Option(False, "--recursive", "-r")
):
    """Вычисление факториала"""
    try:
        if recursive:
            result = factorial_recursive(n)
            method = "рекурсивно"
        else:
            result = factorial(n)
            method = "итеративно"
        typer.echo(f"factorial({n}) = {result} ({method})")
    except Exception as e:
        typer.echo(f"Ошибка: {e}")
        raise typer.Exit(1)


@app.command()
def fibo(
    n: int,
    recursive: bool = typer.Option(False, "--recursive", "-r")
):
    """Вычисление числа Фибоначчи"""
    try:
        if recursive:
            result = fibo_recursive(n)
            method = "рекурсивно"
        else:
            result = fibo(n)
            method = "итеративно"
        typer.echo(f"fibo({n}) = {result} ({method})")
    except Exception as e:
        typer.echo(f"Ошибка: {e}")
        raise typer.Exit(1)


@app.command()
def stack(operations: Optional[List[str]] = typer.Argument(None)):
    """Работа со стеком. Операции: push:X, pop, peek, size"""
    s = Stack()

    if not operations:
        typer.echo("Пример: stack push:10 push:20 peek pop")
        return

    for op in operations:
        if op.startswith("push:"):
            value = float(op.split(":")[1])
            s.push(value)
            typer.echo(f"push({value})")
        elif op == "pop":
            if not s.is_empty():
                val = s.pop()
                typer.echo(f"pop() = {val}")
            else:
                typer.echo("Стек пуст")
        elif op == "peek":
            if not s.is_empty():
                val = s.peek()
                typer.echo(f"peek() = {val}")
            else:
                typer.echo("Стек пуст")
        elif op == "size":
            typer.echo(f"Размер: {len(s)}")
        elif op == "empty":
            typer.echo(f"Пуст: {s.is_empty()}")
        else:
            typer.echo(f"Неизвестная операция: {op}")

    typer.echo(f"Итоговый размер стека: {len(s)}")


if __name__ == "__main__":
    app()
