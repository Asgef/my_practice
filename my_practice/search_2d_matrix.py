# Task: "Search a 2D Matrix"
# Given: m x n integer matrix matrix with the following two properties:
# 1. Each row is sorted in non-decreasing order.
# 2. The first integer of each row is greater than the last integer of the
# previous row.
#
# Given an integer target, return true if target is in the matrix, otherwise
# return false.
#
# You must write a solution with O(log(m * n)) time complexity.
#
#
# Задача: "Поиск двумерной матрицы"
# Дано: m x n целочисленная матрица matrix со следующими двумя свойствами:
# 1. Каждая строка сортируется в неубывающем порядке.
# 2. Первое целое число каждой строки больше последнего целого числа
# предыдущей строки.
#
# Дано целое число target, вернуть true, если target присутствует в matrix,
# иначе вернуть false.
#
# Вы должны написать решение с временной сложностью O(log(m * n)).
#
#
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# binary_search


from typing import List


class Solution:
    def searchMatrix(
            self, matrix: List[List[int]], target: int
    ) -> bool:
        for line in matrix:
            if line[len(line) - 1] > target > line[0]:
                return self.bnr_srch(line, target)
            return False

    def bnr_srch(self, line, target):
        first = 0
        last = len(line) - 1

        while first <= last:
            mid = (first + last) // 2

            if line[mid] == target:
                return True
            elif line[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
        return False
