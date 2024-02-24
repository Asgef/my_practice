# Problem: Longest Consecutive Ones
#
# Given an array consisting of zeroes and ones, write a function to find the
# length of the longest consecutive sequence of ones in the array.
#
# Examples:
# [1,1,0,1,1,1,1] -> 4
# [0,0,0] -> 0
# [1,1,0,1] -> 2


# Задача: Самая длинная последовательность единиц
#
# Дан массив, состоящий из нулей и единиц. Напишите функцию, которая находит
# длину самой длинной последовательности единиц в массиве.
#
# Примеры:
# [1,1,0,1,1,1,1] -> 4
# [0,0,0] -> 0
# [1,1,0,1] -> 2


def max_consecutive_ones(nums):
    result = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            result = max(count, result)
            count = 0
    result = max(count, result)

    return result
