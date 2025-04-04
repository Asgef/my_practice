# Задача: "Разделение Меток"
# Дана строка s. Мы хотим разделить строку на как можно больше частей,
# так чтобы каждая буква встречалась не более чем в одной части.
# Например, строку "ababcc" можно разделить на ["abab", "cc"],
# но такие разделения как ["aba", "bcc"] или ["ab", "ab", "cc"]
# являются недопустимыми.
# Обратите внимание, что разделение выполняется так, чтобы после
# конкатенации всех частей в порядке, результирующая строка должна быть s.
# Верните список целых чисел, представляющих размер этих частей.
#
#
# Task: "Partition Labels"
# You are given a string s. We want to partition the string into as many parts
# as possible so that each letter appears in at most one part.
# For example, the string "ababcc" can be partitioned into ["abab", "cc"],
# but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.
# Note that the partition is done so that after concatenating all the parts
# in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.
#
# Example 1:
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect,
# because it splits s into less parts.
#
# Example 2:
# Input: s = "eccbbbbdec"
# Output: [10]


from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        right, size = 0, 0
        result, map_array = [], {char: idx for idx, char in enumerate(s)}

        for left, cur_char in enumerate(s):
            size += 1
            right = max(right, map_array[cur_char])

            if left == right:
                result.append(size)
                size = 0
        return result
