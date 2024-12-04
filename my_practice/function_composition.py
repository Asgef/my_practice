# Task: "Function Composition"
#
# Implement the function `compose()` that takes two single-argument functions
# as input and returns a new function. This new function should accept one
# argument and apply the original functions in the order `f(g(x))`.
#
#
# Задача: "Композиция функций"
#
# Реализуйте функцию `compose()`, которая принимает на вход две одноаргументные
# функции и возвращает новую функцию. Эта новая функция должна принимать один
# аргумент и применять к нему исходные функции в порядке `f(g(x))`.
#
#
# Example:
#
# def add5(x):
#     return x + 5
#
# def mul3(x):
#     return x * 3
#
# compose(mul3, add5)(1)  # 18
# compose(add5, mul3)(1)  # 8
# compose(mul3, str)(1)   # '111'
# compose(str, mul3)(1)   # '3'
#


def compose(f, g):
    def inner(x):
        return f(g(x))

    return inner
