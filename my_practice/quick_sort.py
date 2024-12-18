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
from numpy.random import default_rng
from pandas import pivot


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


def quick_sort(items: list, direction: str = 'asc') -> list:  # noqa C901
    def partition(array, left, right, pivot, comp):
        while True:
            while comp(array[left], pivot):
                left += 1
            while comp(pivot, array[right]):
                right -= 1

            if left >= right:
                return right + 1

            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    def sort(array, left, right, comp):
        length = right - left + 1
        if length < 2:
            return
        pivot = array[(right + left) // 2]
        split_idx = partition(array, left, right, pivot, comp)
        sort(array, left, split_idx - 1, comp)
        sort(array, split_idx, right, comp)

    cp_items = items[:]
    compare = lambda a, b: a < b if direction == 'asc' else a > b  # noqa E731
    sort(cp_items, 0, len(items) - 1, compare)
    return cp_items


# A clearer but less efficient version of the function


def quick_sort_2(array: list, reverse: bool = False) -> list:  # noqa F811
    cp_array = array[:]
    cmpr = lambda a_arg, b_arg: a_arg < b_arg \
        if reverse is False else a_arg > b_arg  # noqa E731

    if len(cp_array) <= 1:
        return cp_array

    pivot = cp_array[len(cp_array) // 2]
    lower_arr = []
    higher_arr = []
    equal_arr = []

    for elmt in cp_array:
        if cmpr(elmt, pivot):
            lower_arr.append(elmt)
        elif cmpr(pivot, elmt):
            higher_arr.append(elmt)
        else:
            equal_arr.append(elmt)

    return (
            quick_sort_2(lower_arr, reverse) + equal_arr +
            quick_sort_2(higher_arr, reverse)
    )

# Быстрая сортировка
