# Task: Fibonacci Numbers
#
# Implement the function `fib()`, which finds positive Fibonacci numbers.
# The argument of the function is the position of the Fibonacci number.
#
#
# Задача: Числа Фибоначчи
#
# Реализуйте функцию `fib()`, которая находит положительные числа Фибоначчи.
# Аргументом функции является порядковый номер числа.
# Formula:
# f(0) = 0
# f(1) = 1
# f(n) = f(n-1) + f(n-2)
#
# Example:
# fib(3)  # 2
# fib(5)  # 5
# fib(10)  # 55


def fib(n: int) -> int:
    if n == 0:
        return n
    elif n < 3:
        return 1
    return fib(n - 2) + fib(n - 1)

# Train with a generator


def gen_fib():
    current, last = 1, 0
    while True:
        yield current
        current, last = current + last, current

# Fibonacci, generator, infinite iterator.
