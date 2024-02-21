# Longest Consecutive Ones with One Flip
#
# Given an array consisting of zeroes and ones, write a function to find the
# length of the longest consecutive sequence of ones in the array, with the
# ability to flip one zero to one.
#
# Example:
#
# For the array [1,0,1], one flip is possible to obtain [1,1,1].
# The length of the longest consecutive sequence of ones is 3.
#
# For the array [1,0,1,0,1,1], multiple options are possible:
#
# Flip the second element: [1,1,1,0,1,1]. The length of the consecutive
# sequence of ones is 4.
# Flip the fourth element: [1,0,1,1,1,1]. The length of the consecutive
# sequence of ones is also 4.
# You are required to write a function max_consecutive_onesII(nums) which takes
# the array nums as input and returns an integer representing the length of the
# longest consecutive sequence of ones with one flip.
#
# Examples:
#
#
# max_consecutive_onesII([1,0,1])  # Output: 3
# max_consecutive_onesII([1,0,1,0,1,1])  # Output: 4
# max_consecutive_onesII([1,1,1,0,1,1])  # Output: 3
# max_consecutive_onesII([1,0,1,1,1,1])  # Output: 4


# Самая длинная последовательность единиц с одним переворотом
#
# Дан массив, состоящий из нулей и единиц. Необходимо написать функцию,
# которая находит самую длинную последовательность единиц в массиве, при
# условии, что есть возможность перевернуть один элемент с нуля на единицу.
#
# Пример:
#
# Для массива [1,0,1] возможно одно переключение, чтобы получить [1,1,1].
# Длина самой длинной последовательности единиц равна 3.
#
# Для массива [1,0,1,0,1,1] возможны несколько вариантов:
#
# Переключить второй элемент: [1,1,1,0,1,1]. Длина последовательности
# единиц равна 4.
# Переключить четвёртый элемент: [1,0,1,1,1,1]. Длина последовательности
# единиц также равна 4.
# Требуется написать функцию max_consecutive_onesII(nums), которая принимает
# массив nums и возвращает целое число, представляющее длину самой длинной
# последовательности единиц с одним переворотом.


def max_consecutive_onesII(nums):
    pointer_head = 0
    pointer_tail = 0
    count_null = 0
    coup_site = 0
    result = 0
    for idx, elem in enumerate(nums):
        pointer_head = idx
        if elem == 1:
            continue
        elif elem == 0:
            result = max(pointer_head - pointer_tail, result)
            count_null += 1
            pointer_tail = coup_site
            coup_site = idx
    if count_null == 1:
        result = max(pointer_head - coup_site, result)
    else:
        result = max(pointer_head - pointer_tail, result)
    return result
