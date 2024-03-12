# Problem: Find Rotation Point
# Given a sorted array of unique integers that has been rotated at an unknown pivot,
# find and return the index of the minimum element (the rotation point).
# Assume no duplicate elements exist in the array.
# Example 1: Input: nums = [4, 5, 6, 7, 0, 1, 2], Output: 4
# Example 2: Input: nums = [3, 4, 5, 1, 2], Output: 3


# Задача: Найти точку вращения в отсортированном массиве
# Дан отсортированный массив уникальных целых чисел, который был повернут в неизвестной точке,
# найти и вернуть индекс минимального элемента (точку вращения).
# Предполагается, что в массиве нет дублирующих элементов.
# Пример 1: Вход: nums = [4, 5, 6, 7, 0, 1, 2], Вывод: 4
# Пример 2: Вход: nums = [3, 4, 5, 1, 2], Вывод: 3


def find_rotation_point(sequence):
    if not sequence:
        return -1

    first, last = 0, len(sequence) - 1

    if sequence[first] < sequence[last]:
        return 0

    while first <= last:
        mid = (first + last) // 2

        if mid + 1 < len(sequence) and sequence[mid] > sequence[mid + 1]:
            return mid + 1
        if mid - 1 >= 0 and sequence[mid - 1] > sequence[mid]:
            return mid

        if sequence[mid] > sequence[last]:
            first = mid + 1
        else:
            last = mid - 1

    return -1
