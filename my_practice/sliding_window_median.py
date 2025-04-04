# Задача: "Медиана Скользящего Окна"
# Медиана — это среднее значение в упорядоченном списке целых чисел.
# Если размер списка четный, то медианы нет. В этом случае медиана — это
# среднее двух средних значений.
#
# Например, если arr = [2,3,4], медиана равна 3.
# Например, если arr = [1,2,3,4], медиана равна (2 + 3) / 2 = 2.5.
# Вам дан целочисленный массив nums и целое число k.
# Существует скользящее окно размером k, которое перемещается от самого
# левого края массива до самого правого. Вы можете видеть только k чисел
# в окне. Каждый раз, когда скользящее окно перемещается вправо на одну
# позицию.
#
# Верните массив медиан для каждого окна в оригинальном массиве.
#
# Task: "Sliding Window Median"
# You are given an integer array nums and an integer k.
# There is a sliding window of size k which is moving from the very left
# of the array to the very right. You can only see the k numbers in the
# window. Each time the sliding window moves right by one position.
#
# Return the median array for each window in the original array.
#
# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
# Explanation:
# Window position                Median
# ---------------                -----
# [1  3  -1] -3  5  3  6  7        1
# 1 [3  -1  -3] 5  3  6  7       -1
# 1  3 [-1  -3  5] 3  6  7       -1
# 1  3  -1 [-3  5  3] 6  7        3
# 1  3  -1  -3 [5  3  6] 7        5
# 1  3  -1  -3  5 [3  6  7]       6
#
# Example 2:
# Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
# Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]


import bisect
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = 0
        window, result = [], []

        if len(nums) < k:
            return result

        for right, cur_el in enumerate(nums):
            bisect.insort(window, cur_el)

            if len(window) == k:
                if k % 2 != 0:
                    result.append(float(window[k // 2]))
                else:
                    result.append(
                        (window[(k // 2) - 1] + window[k // 2]) / 2
                    )

                idx = bisect.bisect_left(window, nums[left])
                window.pop(idx)
                left += 1
        return result


# Скользящее окно, бинарный поиск, две точки, two pointers, sliding window
# binary search.
