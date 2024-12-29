# Задача: "Слияние интервалов"
# Дан массив интервалов, где intervals[i] = [starti, endi].
# Необходимо объединить все пересекающиеся интервалы и вернуть массив
# непересекающихся интервалов, покрывающих все входные интервалы.
#
#
# Task: "Merge Intervals"
# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals and return an array of the non-overlapping
# intervals.
#
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
#
# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        current = intervals[0]

        for idx in range(1, len(intervals)):
            if intervals[idx][0] <= current[1]:
                current[1] = max(current[1], intervals[idx][1])
            else:
                result.append(current)
                current = intervals[idx]
        result.append(current)
        return result
