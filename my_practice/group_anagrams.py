# Task: Group Anagrams
#
# Given an array of strings 'strs', group the anagrams together.
# You can return the answer in any order.
#
# Задача: Группировка Анаграмм
#
# Дан массив строк 'strs', сгруппируйте вместе анаграммы.
# Ответ можно вернуть в любом порядке.
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        passed = {}

        for elem in strs:
            key = ''.join(sorted(elem))
            if key not in passed:
                passed[key] = []
                passed[key].append(elem)
            else:
                passed[key].append(elem)
        result = passed.values()
        return result

# Хеш таблица.
