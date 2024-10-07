# Task: Find All Anagrams in a String
#
# Given two strings 's' and 'p', return an array of all the start indices of
# p's anagrams in 's'. The answer can be returned in any order.
#
#
# Задача: Найти все анаграммы в строке
#
# Даны две строки 's' и 'p'. Верните массив всех начальных индексов анаграмм
# строки 'p' в строке 's'. Порядок может быть произвольным.
#
#
# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation: Substrings at indices 0 ("cba")
# and 6 ("bac") are anagrams of "abc".
#
# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation: Substrings at indices 0 ("ab"), 1 ("ba"), and 2 ("ab") are
# anagrams of "ab".


from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []

        result = []

        for idx in range(len(s) - len(p) + 1):
            word = s[idx: idx + len(p)]
            if not Counter(word) - Counter(p):
                result.append(idx)
        return result
