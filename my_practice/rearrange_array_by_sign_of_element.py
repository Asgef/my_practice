# Problem: Rearrange Array by Sign
#
# Given an array consisting of positive (n > 0) and negative (n < 0) numbers,
# rearrange the array in such a way that:
# - each consecutive pair has opposite signs;
# - the sequence of numbers with the same signs remains unchanged after
#   rearrangement;
# - the first element is always positive.
#
# Example:
# [-4, 3, 1, -2, 1, -3] -> [3, -4, 1, -2, 1, -3]
# [1, 2, 3, -3, -1, -2] -> [1, -3, 2, -1, 3, -2]


# Задача: Перестановка массива по знаку элемента
#
# Дан массив, который состоит из положительных (n > 0) и отрицательных (n < 0)
# чисел. Необходимо переставить массив таким образом, чтобы:
# - каждая последовательная пара имела противоположные знаки;
# - последовательность чисел с одинаковыми знаками оставалась неизменной после
#   перестановки;
# - первый элемент всегда был положительным.
#
# Пример:
# [-4, 3, 1, -2, 1, -3] -> [3, -4, 1, -2, 1, -3]
# [1, 2, 3, -3, -1, -2] -> [1, -3, 2, -1, 3, -2]


def rearrange_array(nums: list) -> list:
    positive = 0
    negative = 1
    result = [None] * len(nums)

    for elem in nums:
        if elem > 0:
            result[positive] = elem
            positive += 2
        else:
            result[negative] = elem
            negative += 2
    return result
