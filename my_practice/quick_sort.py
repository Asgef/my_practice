# Problem: Implementing Quick Sort Algorithm
#
# Implement a function that sorts an array of numbers using the quick sort
# algorithm. The function accepts an array of numbers as the first argument
# and the sorting direction (asc or desc) as the second argument, with 'asc'
# being the default. The function should not mutate the original array.
# Example usage:
# solution([10, 20, 0, -1]) # Returns [-1, 0, 10, 20]
# solution([]) # Returns []
# solution([10, 20, 0, -1], 'desc') # Returns [20, 10, 0, -1]


# Задача: Реализация алгоритма быстрой сортировки
#
# Реализуйте функцию, которая сортирует массив чисел используя алгоритм
# быстрой сортировки. Функция принимает первым аргументом массив чисел и
# направление сортировки (asc или desc) вторым аргументом, причем по умолчанию
# направление равно asc. Функция не должна мутировать исходный массив.
# Пример использования:
# solution([10, 20, 0, -1]) # Возвращает [-1, 0, 10, 20]
# solution([]) # Возвращает []
# solution([10, 20, 0, -1], 'desc') # Возвращает [20, 10, 0, -1]


def partition(items, left, right, pivot, compare):
    while True:

        while compare(items[left], pivot):
            left += 1
        while compare(pivot, items[right]):
            right -= 1

        if left >= right:
            return right + 1

        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1


def sort(items, left, right, compare):
    length = right - left + 1
    if length < 2:
        return

    pivot = items[left]
    split_idx = partition(items, left, right, pivot, compare)
    sort(items, left, split_idx - 1, compare)
    sort(items, split_idx, right, compare)


def solution(items, direction='asc'):
    result = items[:]
    compare = lambda a, b: a < b if direction == 'asc' else a > b
    sort(result, 0, len(items) - 1, compare)
    return result
