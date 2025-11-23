from copy import deepcopy
import time


def timeit_once(func, *args, **kwargs) -> float:
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    func_time = end_time - start_time
    return (f"Функция выполнилась за: {(func_time):.5f}")


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, callable]) -> dict[str, dict[str, float]]:
    results = {}

    for array_name, array in arrays.items():
        results[array_name] = {}

        for algo_name, algo_func in algos.items():
            array_copy = deepcopy(array)
            time_taken = timeit_once(algo_func, array_copy)
            results[array_name][algo_name] = time_taken

    return results
