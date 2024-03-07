# Problem: Search for the Unique Element in an Array Containing Duplicates
#
# Given a non-empty array of integers nums, where every element appears twice
# except for one. Find the unique element.
#
# Examples:
# [1,1,5,5,3,3,7,4,4] -> 7
# [1,2,1] -> 2


# Задача: Поиск уникального элемента в массиве, содержащем дубликаты
#
# Дан непустой массив целых чисел nums, каждый элемент появляется дважды,
# кроме одного. Найдите уникальный элемент.
# Примеры:
# [1,1,5,5,3,3,7,4,4] -> 7
# [1,2,1] -> 2


# def find_unique_element(sequence):
#     return 2 * sum(set(sequence)) - sum(sequence)


def find_unique_element(sequence):
    res = 0
    for num in sequence:
        res = res ^ num

    return res
