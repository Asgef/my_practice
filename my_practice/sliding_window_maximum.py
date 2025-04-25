# Задача: "Максимум в скользящем окне"
# Дан массив целых чисел и размер окна k. Окно движется слева направо,
# сдвигаясь на одну позицию за шаг. Нужно вернуть максимум в каждом окне.
#
# Task: "Sliding Window Maximum"
# You are given an array of integers and a window size k. The window slides
# from the left to the right, one position at a time. Return the maximum
# value in each window.
#
# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]


from typing import List
from collections import deque


# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         result = []
#         window = deque()
#         left, right = 0, 0
#
#         while right < len(nums):
#             while window and nums[window[-1]] < nums[right]:
#                 window.pop()
#
#             window.append(right)
#
#             if left > window[0]:
#                 window.popleft()
#
#             if right + 1 >= k:
#                 result.append(nums[window[0]])
#                 left += 1
#             right += 1
#         return result


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()
        left = 0

        for right in range(len(nums)):
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()
            if right + 1 >= k:
                result.append(nums[q[0]])
                left += 1
        return result


# sliding window, two pointers, queue
