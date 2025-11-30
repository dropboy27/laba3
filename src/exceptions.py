class NegativeNumberError(Exception):
    def __init__(self, number):
        self.number = number
        message = f"Число {number} меньше нуля"
        super().__init__(message)


class EmptyStackError(IndexError):
    """Попытка извлечь (pop) или посмотреть (peek) элемент из пустого стека."""
    pass
