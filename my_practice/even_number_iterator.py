# Task: Even Number Iterator
#
# Create an iterator using a class that returns only even numbers from 1 to 20.
#
#
# Задача: Итератор Четных Чисел
#
# Создайте итератор через класс, который возвращает только чётные числа
# от 1 до 20.
#
# Example usage:
# iterator = EvenIterator()
# for num in iterator:
#     print(num)
# Output:
# 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
from PIL.ImageSequence import Iterator


class EvenIterator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > 20:
            raise StopIteration
        return self.current
