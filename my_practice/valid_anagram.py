# Task: Valid Anagram
#
# Given two strings 's' and 't', return true if 't' is an anagram of 's',
# and false otherwise.
#
# Задача: Проверка на анаграмму
#
# Даны две строки 's' и 't'. Верните true, если 't' является анаграммой
# строки 's', иначе верните false.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: false


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
