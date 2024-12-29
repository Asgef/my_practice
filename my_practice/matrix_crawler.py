# Task: "Matrix crawler"
#
# Implement a function that takes a square matrix (2D list) and returns
# a list of elements ordered in a counter-clockwise spiral, starting
# from the top-left element.
#
#
# Задача: "матричный обходчик"
#
# Реализуйте функцию, которая принимает квадратную матрицу (двумерный
# список) и возвращает список элементов, упорядоченных по спирали
# против часовой стрелки, начиная с верхнего левого элемента.
#
# Examples:
#
# Example 1: Input: matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# nums = [1, 5, 9, 13, 14, 15, 16, 12, 8, 4, 3, 2, 6, 10, 11, 7]
#
# Example 2: Input: matrix = [
#     [1, 2],
#     [3, 4]
# ]
# enums = [1, 3, 4, 2]
#
# Example 1: Input: matrix = [[1]]
# nums = [1]
#
# Requirements:
#
# - The function should work with any square matrix, sizes 1x1 and up.
# - The returned list should contain elements ordered in a counter-
#   clockwise spiral.


def matrix_is_square(matrix: list[list[int]]) -> bool:
    return len(matrix) == len(matrix[0])


def matrix_crawler(matrix: list[list[int]]) -> list[int]:  # noqa C901
    if len(matrix) == 1:
        return matrix[0]
    if not matrix or not matrix_is_square(matrix):
        return []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    result = []

    while left <= right and top <= bottom:

        for idx in range(top, bottom + 1):
            result.append(matrix[idx][left])
        left += 1

        for idx in range(left, right + 1):
            result.append(matrix[bottom][idx])
        bottom -= 1

        if left <= right:
            for idx in range(bottom, top - 1, -1):
                # range(top, bottom + 1)[::-1]
                result.append(matrix[idx][right])
            right -= 1

        if top <= bottom:
            for idx in range(right, left - 1, -1):
                result.append(matrix[top][idx])
            top += 1
    return result
