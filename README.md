
# Лабораторная работа 3


Цель: реализовать базовые алгоритмы сортировки, математические функций и структуры данных на Python.

* **Библиотеки:** *typer*
* **Чему я научился:**
    - Написание простых автотестов с помощью pytest
    - Разделение логики по функциям, классам, модулям
    - Реализация стэка
    - Реализация алгоритмов сортировки
    - Реализация математических функций, в том числе рекурсивно
## Реализованные компоненты

### Алгоритмы сортировки

- **Bubble Sort** - пузырьковая сортировка
- **Quick Sort** - быстрая сортировка
- **Heap Sort** - пирамидальная сортировка
- **Counting Sort** - сортировка подсчетом
- **Radix Sort** - поразрядная сортировка
- **Bucket Sort** - блочная сортировка

Алгоритмы поддерживают (кроме radix sort):
- Сортировку произвольных типов через параметр `key`
- Пользовательские функции сравнения через параметр `cmp`

### Математические функции

- **Факториал** - итеративная и рекурсивная реализации
- **Числа Фибоначчи** - итеративная и рекурсивная реализации

Обе функции выбрасывают исключение `NegativeNumberError` для отрицательных чисел.

### Структуры данных

**Stack** - стек с дополнительными возможностями:
- `push(x)` - добавление элемента
- `pop()` - извлечение элемента
- `peek()` - просмотр верхнего элемента
- `is_empty()` - проверка на пустоту
- `__len__()` - получение размера

## Структура проекта

```

laba3/
├──leercode - задачи с литкода
├── src/
│   ├── math/
│   │   ├── factorial_function.py
│   │   ├── factorial_recursive_function.py
│   │   ├── fibo_function.py
│   │   └── fibo_recursive_function.py
│   ├── sortings/
│   │   ├── bubble_sort_function.py
│   │   ├── quick_sort_function.py
│   │   ├── heap_sort_function.py
│   │   ├── counting_sort_function.py
│   │   ├── radix_sort_function.py
│   │   └── bucket_sort_function.py
│   ├── additional_utils/
│   │   ├── should_swap_function.py
│   │   ├── test_cases_generation.py
│   │   ├── benchmarks.py
│   ├── stack_class.py
│   ├── main.py
│   └── exceptions.py
├── tests/
│   ├── test_math.py
│   ├── test_sortings.py
│   └── test_stack.py
├── .gitignore
└── README.md
```

## Установка

### Требования

- Python 3.10+

### Зависимости

```

pip install -r requirements.txt

```

Основные библиотеки:
- `typer` - CLI интерфейс
- `pytest` - тестирование
- `pytest-cov` - покрытие тестами

## Использование

### CLI интерфейс

#### Сортировка массива
python -m src/main.py --help
```

python -m src/main.py sort 5 2 8 1 9
python -m src/main.py sort 5 2 8 1 9 --algo bubble
python -m src/main.py sort 5 2 8 1 9 --algo heap

```

Доступные алгоритмы: `quick`, `bubble`, `heap`, `counting`, `radix`

#### Вычисление факториала

```

python -m src/main.py fact 5
python -m src/main.py fact 10 --recursive

```

#### Вычисление чисел Фибоначчи

```

python -m src/main.py fib 10
python -m src/main.py fib 15 --recursive

```

#### Работа со стеком

```

python -m src/main.py stack push:10 push:20 push:5 peek pop size

```

Доступные операции: `push:X`, `pop`, `peek`, `size`, `empty`


## Технические детали

### Обработка ошибок

- `NegativeNumberError` - передано отрицательное число в factorial/fibonacci
- `EmptyStackError` - попытка pop/peek из пустого стека



### Ограничения

- `list.sort()` и `sorted()` не используются в реализации сортировок
- Counting Sort работает только с целыми числами
- Radix Sort предназначен для неотрицательных целых чисел
- Heap Sort изменяет исходный массив 


