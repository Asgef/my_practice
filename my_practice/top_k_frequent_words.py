# Задача: "Топ K самых частых слов"
# Текст: Дано массив строк words и число k, верните k самых
# частых слов. Отсортируйте по убыванию частоты, а при равной
# частоте — по лексикографическому порядку.
#
# Task: "Top K Frequent Words"
# Text: Given an array of strings words and an integer k, return
# the k most frequent strings. Sort the answer by highest frequency
# first, and lexicographically if frequencies are equal.
#
# Example 1:
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
#
# Example 2:
# Input: words = ["the","day","is","sunny","the","the","the",
# "sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]


from typing import List
from collections import Counter
import heapq


# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         data = list(Counter(words).items())
#         data.sort(key=lambda x: (-x[1], x[0]))
#         return [elem[0] for elem in data[:k]]


# Применим Кучу

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        data = Counter(words)
        heap = []
        result = []

        for word, count in data.items():
            heapq.heappush(heap, (-count, word))

        for _ in range(k):
            _, word = heapq.heappop(heap)
            result.append(word)

        return result
