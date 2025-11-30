import typer
from typing import List
from src.sortings.quick_sort_function import quick_sort
from src.sortings.bubble_sort_function import bubble_sort
from src.sortings.heap_sort_function import heap_sort
from src.math.factorial_function import factorial
from src.math.fibo_function import fibo
from src.stack_class import Stack

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
