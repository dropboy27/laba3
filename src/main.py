import typer
import time
import random
from copy import deepcopy
from typing import List, Optional
from .sortings.quick_sort_function import quick_sort
from .sortings.bubble_sort_function import bubble_sort
from .sortings.heap_sort_function import heap_sort
from .sortings.counting_sort_function import counting_sort
from .sortings.radix_sort_function import radix_sort
from .sortings.bucket_sort_function import bucket_sort
from .math.factorial_function import factorial
from .math.factorial_recursive_function import factorial_recursive
from .math.fibo_function import fibo
from .math.fibo_recursive_function import fibo_recursive
from .stack_class import Stack

app = typer.Typer()

SORT_ALGORITHMS = {
    "quick": quick_sort,
    "bubble": bubble_sort,
    "counting": counting_sort,
    "radix": radix_sort,
    "bucket": bucket_sort,
    "heap": heap_sort
}


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
        "bucket": bucket_sort
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
def fib(
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
    """Работа со стеком. Операции: push:X, pop, peek, size, min"""
    s = Stack()

    if not operations:
        typer.echo("Пример: stack push:10 push:20 peek pop min")
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
        elif op == "min":
            if not s.is_empty():
                val = s.min()
                typer.echo(f"min() = {val}")
            else:
                typer.echo("Стек пуст")
        else:
            typer.echo(f"Неизвестная операция: {op}")

    typer.echo(f"Итоговый размер стека: {len(s)}")


@app.command()
def generate(
    size: int = typer.Option(100, "--size", "-s", help="Размер массива"),
    test_type: str = typer.Option("random", "--type", "-t",
                                  help="Тип тест-кейса: random, sorted, reversed, duplicates"),
    min_val: int = typer.Option(0, "--min", help="Минимальное значение"),
    max_val: int = typer.Option(1000, "--max", help="Максимальное значение"),
):
    """Генерация тест-кейсов для тестирования алгоритмов"""

    if test_type == "random":
        test_case = [random.randint(min_val, max_val) for _ in range(size)]
    elif test_type == "sorted":
        test_case = list(range(min_val, min_val + size))
    elif test_type == "reversed":
        test_case = list(range(min_val + size - 1, min_val - 1, -1))
    elif test_type == "duplicates":
        unique_count = max(1, size // 10)
        test_case = [random.randint(min_val, min_val + unique_count)
                     for _ in range(size)]
    elif test_type == "nearly_sorted":
        test_case = list(range(min_val, min_val + size))
        swaps = size // 10
        for _ in range(swaps):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            test_case[i], test_case[j] = test_case[j], test_case[i]
    else:
        typer.echo(f"Неизвестный тип: {test_type}")
        typer.echo(
            "Доступны: random, sorted, reversed, duplicates, nearly_sorted")
        raise typer.Exit(1)

    typer.echo(f"Сгенерирован тест-кейс ({test_type}): размер={size}")

    typer.echo(f"Массив: {test_case}")


@app.command()
def benchmark(
    size: int = typer.Option(100, "--size", "-s",
                             help="Размер массива для бенчмарка"),
    algorithms: Optional[List[str]] = typer.Option(None, "--algo", "-a",
                                                   help="Алгоритмы для тестирования"),
):
    """Бенчмарк алгоритмов сортировки"""

    if algorithms:
        algos_to_test = {name: SORT_ALGORITHMS[name] for name in algorithms
                         if name in SORT_ALGORITHMS}
        if not algos_to_test:
            typer.echo("Не найдено подходящих алгоритмов")
            raise typer.Exit(1)
    else:
        algos_to_test = SORT_ALGORITHMS

    typer.echo(f"Бенчмарк алгоритмов сортировки")
    typer.echo(f"Размер массива: {size}")

    test_cases = {
        "random": [random.randint(0, 10000) for _ in range(size)],
        "sorted": list(range(size)),
        "reversed": list(range(size-1, -1, -1))
    }

    results = {}

    for test_name, test_array in test_cases.items():
        typer.echo(f"\nТестирование на массиве: {test_name}")
        results[test_name] = {}

        for algo_name, algo_func in algos_to_test.items():
            times = []

            array_copy = deepcopy(test_array)

            start_time = time.perf_counter()

            if algo_name == "heap":
                algo_func(array_copy)
            else:
                _ = algo_func(array_copy)

            end_time = time.perf_counter()
            times.append(end_time - start_time)

            avg_time = sum(times) / len(times)
            results[test_name][algo_name] = avg_time

            typer.echo(f"  {algo_name:15s}: {avg_time:.6f} сек")

    header = f"{'Алгоритм':<15}"
    for test_name in test_cases.keys():
        header += f"{test_name:>15}"
    typer.echo(header)
    typer.echo("-" * 60)

    for algo_name in algos_to_test.keys():
        row = f"{algo_name:<15}"
        for test_name in test_cases.keys():
            time_val = results[test_name][algo_name]
            row += f"{time_val:>15.6f}"
        typer.echo(row)


if __name__ == "__main__":
    app()
