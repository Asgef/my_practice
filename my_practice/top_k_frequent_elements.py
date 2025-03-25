# Задача: "Топ K Частых Элементов"
# Дано целочисленный массив nums и целое число k,
# верните k самых частых элементов.
# Ответ может быть возвращен в любом порядке.
#
# Task: "Top K Frequent Elements"
# Given an integer array nums and an integer k,
# return the k most frequent elements.
# You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]


from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data_nums = Counter(nums)
        heap = []
        result = []

        for num, count in data_nums.items():
            heapq.heappush(heap, (-count, num))

        for _ in range(k):
            _, num = heapq.heappop(heap)
            result.append(num)
        return result
