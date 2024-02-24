# Problem: Longest Consecutive Ones with One Flip
#
# Given an array consisting of zeroes and ones, write a function to find the
# length of the longest consecutive sequence of ones in the array, with the
# ability to flip one zero to one.
#
# Example:
# For the array [1,0,1], one flip is possible to obtain [1,1,1]. The length
# of the longest consecutive sequence of ones is 3.
#
# For the array [1,0,1,0,1,1], multiple options are possible:
# 1. Flip the second element: [1,1,1,0,1,1]. The length of the consecutive
#    sequence of ones is 3.
# 2. Flip the fourth element: [1,0,1,1,1,1]. The length of the consecutive
#    sequence of ones is also 3.
#
# You are required to write a function max_consecutive_onesII(nums) which
# takes the array nums as input and returns an integer representing the length
# of the longest consecutive sequence of ones with one flip.
#
# Examples:
# print(max_consecutive_onesII([1,0,1]))    # Output: 3
# print(max_consecutive_onesII([1,0,1,0,1,1]))  # Output: 4
# print(max_consecutive_onesII([1,1,1,0,1,1]))  # Output: 6
# print(max_consecutive_onesII([1,0,1,1,1,1]))  # Output: 6


# Задача: Самая длинная последовательность единиц с одним переворотом
#
# Дан массив, состоящий из нулей и единиц. Необходимо написать функцию,
# которая находит длину самой длинной последовательности единиц в массиве,
# с возможностью перевернуть один ноль в единицу.
#
# Пример:
# Для массива [1,0,1] одно переключение возможно для получения [1,1,1].
# Длина самой длинной последовательности единиц равна 3.
#
# Для массива [1,0,1,0,1,1] существует несколько вариантов:
# 1. Переключить второй элемент: [1,1,1,0,1,1]. Длина последовательности
#    единиц равна 3.
# 2. Переключить четвёртый элемент: [1,0,1,1,1,1]. Длина последовательности
#    единиц также равна 3.
#
# Требуется написать функцию max_consecutive_onesII(nums), которая принимает
# массив nums в качестве входных данных и возвращает целое число,
# представляющее длину самой длинной последовательности единиц с одним
# переворотом.
#
#
# Примеры:
# print(max_consecutive_onesII([1,0,1]))    # Вывод: 3
# print(max_consecutive_onesII([1,0,1,0,1,1]))  # Вывод: 4
# print(max_consecutive_onesII([1,1,1,0,1,1]))  # Вывод: 6
# print(max_consecutive_onesII([1,0,1,1,1,1]))  # Вывод: 6


def max_consecutive_onesII(nums):
    result = 0
    current_length = 0
    count_ones_before_flip = 0
    for elem in nums:
        if elem == 1:
            current_length += 1
        else:  # elem == 0
            result = max(result, count_ones_before_flip + current_length + 1)
            count_ones_before_flip = current_length
            current_length = 0
    result = max(result, count_ones_before_flip + current_length + 1)
    return result
