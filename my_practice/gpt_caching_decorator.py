# Task: Caching Decorator
#
# Write a decorator that caches the results of a function. When the function
# is called with the same arguments again, the decorator should return the
# stored result from the cache instead of computing it again.
#
# The decorator should handle both positional and keyword arguments and
# should work with various data types, including cases like 1 and 1.0.
#
#
# Задача: Декоратор для кэширования результатов
#
# Напишите декоратор, который будет кэшировать результаты выполнения функции.
# Когда функция вызывается с теми же аргументами, декоратор должен возвращать
# сохранённый результат из кэша, а не вычислять его заново.
#
# Декоратор должен поддерживать позиционные и именованные аргументы, а также
# корректно обрабатывать разные типы данных.
#
# Example usage:
# @cache_decorator
# def add(a, b):
#     return a + b
#
# result1 = add(1, 2)  # First call: result is computed
# result2 = add(1, 2)  # Second call: result is retrieved from cache
# result3 = add(2, 3)  # New call: result is computed


def cache_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

# Кеширующий декоратор
