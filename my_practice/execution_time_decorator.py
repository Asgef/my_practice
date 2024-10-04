# Task: Execution Time Decorator
#
# Create a decorator that measures the execution time of a function and
# prints it to the screen.
#
#
# Задача: Декоратор для измерения времени выполнения
#
# Создайте декоратор, который измеряет время выполнения функции и выводит его
# на экран.
#
# Example usage:
# @time_decorator
# def some_function():
#     # Some code here
#
# some_function()
# Output:
# Execution time: X.XXXXXX seconds

import time
from time import sleep



def time_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Начало выполнения функции {func.__name__}')
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        print(f'Конец выполнения функции {func.__name__}')
        print(
            f'Время работы функции {func.__name__}: '
            f'{time_end - time_start} секунды'
        )
        return result
    return wrapper

@ time_decorator
def square_root(num):
    sleep(1)
    return num ** 0.5


print(square_root(25))

# root, корень числа, square, декоратор, decorator, time.
