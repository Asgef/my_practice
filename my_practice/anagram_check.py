# Task: Anagram Check
# Write a function to check if two strings are anagrams of each other.
# An anagram is a rearrangement of the letters of one word or phrase
# to form another.
# For this task, it doesn't matter if the resulting word makes sense;
# we treat them simply as strings and check if one string can be formed
# from the other.
#
# String 1: 'Aba'
# String 2: 'aab'
# Answer: True


# Задача: Проверка анаграмм
# Напишите функцию, которая проверяет, является ли строки
# анаграммами друг друга.
# Анаграмма это составление из букв одного слова другого.
# Для задачи не важно чтобы слово реально существовало; мы их рассматриваем
# просто как строки и проверяем можно ли из одной строки составить другую.
#
# Строка 1: 'Aba'
# Строка 2: 'aab'
# Ответ: True


def are_anagrams(str1, str2):
    count_str1 = {}
    count_str2 = {}
    for i in str1.lower():
        count_str1[i] = count_str1.get(i, 0) + 1

    for i in str2.lower():
        count_str2[i] = count_str2.get(i, 0) + 1

    return count_str1 == count_str2
