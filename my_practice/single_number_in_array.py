# Task: Single Number
# Difficulty: Easy
#
# Given a non-empty array 'nums' of integers, every element appears twice
# except for one. Find that single element.
#
# You must implement a solution with linear time complexity and use only
# constant extra space.


# Задача: Одинокое Число
# Сложность: Легкая
#
# Дан непустой массив 'nums' целых чисел, в котором каждый элемент встречается
# дважды, кроме одного. Найдите это число.
#
# Необходимо реализовать решение с линейной временной сложностью и
# постоянной дополнительной памятью.

#
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
#
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
#
# Example 3:
# Input: nums = [1]
# Output: 1


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num
        return result

# Битовая операция XOR, исключающее ИЛИ.
