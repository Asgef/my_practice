# Task: Binary Search
# Given a sorted array of integers and a target value,
# return the index of the target
# if found, or -1 if it is not present in the array.
# Example 1: Input: nums = [-5, 2, 4, 6, 9], target = 4, Output: 2
# Example 2: Input: nums = [1, 2, 3, 4, 5], target = 6, Output: -1


# Задача: Бинарный поиск
# Дан отсортированный массив целых чисел и целевое значение,
# вернуть индекс цели,
# если она найдена, или -1, если её нет в массиве.
# Пример 1: Вход: nums = [-5, 2, 4, 6, 9], цель = 4, Вывод: 2
# Пример 2: Вход: nums = [1, 2, 3, 4, 5], цель = 6, Вывод: -1


from typing import List


def binary_search(sequence, num):
    sequence_len = len(sequence)

    if sequence_len == 0:
        return -1

    first = 0
    last = sequence_len - 1

    while first <= last:
        middle = (first + last) // 2

        if sequence[middle] == num:
            return middle

        if sequence[middle] < num:
            last = middle - 1
        else:
            first = middle + 1

    return -1


# For leetcode

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        first, last = 0, len(nums) - 1

        if not nums:
            return -1

        while first <= last:
            mid = first + (last - first) % 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1
        return -1

# Бинарный поиск
