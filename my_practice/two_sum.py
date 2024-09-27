# Task: Two Sum
#
# Given an array of integers 'nums' and an integer 'target', return the
# indices of the two numbers such that they add up to 'target'.
#
# You may assume that each input would have exactly one solution, and you
# may not use the same element twice.
#
# You can return the answer in any order.
#
#
# Задача: Два числа
#
# Дано: массив целых чисел 'nums' и целое число 'target'. Верните индексы
# двух чисел, сумма которых равна 'target'.
#
# Вы можете предположить, что существует ровно одно решение, и вы не можете
# использовать один и тот же элемент дважды.
#
# Ответ можно вернуть в любом порядке.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] == 9, so we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1, 2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0, 1]


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed_elem = {}

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in passed_elem:
                return [passed_elem[complement], idx]
            passed_elem[num] = idx
        return []


# Хэш таблицы.
