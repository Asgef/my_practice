# Задача: "Замена символов для самой длинной повторяющейся подстроки"
# Дана строка s и целое число k. Разрешено изменить не более k символов
# строки, заменив их на любые заглавные английские буквы. Верните длину
# самой длинной подстроки, состоящей из одинаковых символов, которую можно
# получить после этих замен.
#
# Task: "Longest Repeating Character Replacement"
# You are given a string s and an integer k. You can change at most k
# characters in the string to any uppercase English letter. Return the
# length of the longest substring that contains the same letter after
# the replacements.
#
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
#
# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace one 'A' with 'B' to get "AABBBBA" → "BBBB"


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        left = 0
        max_len = 0
        max_count = 0

        for right in range(len(s)):
            hash_map[s[right]] = 1 + hash_map.get(s[right], 0)
            max_count = max(max_count, hash_map[s[right]])

            if (right - left + 1) - max_count > k:
                hash_map[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


# sliding window, two pointers, hashmap, defaultdict.
