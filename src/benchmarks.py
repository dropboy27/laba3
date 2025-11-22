import time


def timeit_once(func, *args, **kwargs) -> float:
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    func_time = end_time - start_time
    return (f"Функция выполнилась за: {(func_time):.3f}")


def benchmark_sorts(arrays: dict[str, list], algos: dict[str,
                    callable]) -> dict[str, dict[str, float]]: ...
