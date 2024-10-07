# Problem: Find Minimum in Rotated Sorted Array
#
# Given an array of length n sorted in ascending order that was rotated
# between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7]
# might become:
#
# - [4,5,6,7,0,1,2] if rotated 4 times.
# - [0,1,2,4,5,6,7] if rotated 7 times.
#
# Task: Write an algorithm that finds the minimum element in such an array.
# Your solution must run in O(log n) time.
#
#
#
# Задача: Найти минимальное значение в повернутом отсортированном массиве
#
# Вам дан массив длиной n, отсортированный по возрастанию, который был
# повёрнут от 1 до n раз. Например, массив nums = [0,1,2,4,5,6,7] может стать:
#
# - [4,5,6,7,0,1,2] если его повернули 4 раза.
# - [0,1,2,4,5,6,7] если его повернули 7 раз.
#
# Задача: Написать алгоритм, который находит минимальный элемент в таком
# массиве. Ваша программа должна работать за O(log n) времени.
#
# Examples:
#
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] and was rotated 3 times.
#
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and was rotated 4 times.
#
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and was rotated 4 times.


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:  # noqa C901
        first, last = 0, len(nums) - 1

        if not nums:
            return -1
        if len(nums) == 1 or nums[first] < nums[last]:
            return nums[0]

        while first < last:
            mid = first + (last - first) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[last]:
                first = mid + 1
            else:
                last = mid - 1
        return nums[mid]

# бинарный поиск.
