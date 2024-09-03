# Problem: Definition of a Prime Number
# Implement a function that checks whether a number is prime or not.
# Example usage:
# is_prime(3) Returns True
# is_prime(4) Returns False

# Задача: Определение простого числа
# Реализуйте функцию, которая проверяет, является ли число простым или нет.
# Пример использования:
# is_prime(3) Возвращает True
# is_prime(4) Возвращает False


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 1/2) + 1):
        if num % i == 0:
            return False
    return True
