# Task: "Scrabble"
# Implement the predicate function scrabble, which takes two parameters: a set
# of characters (a string) and a word. The function should check if the word
# can be formed from the given set of characters. The function returns True or
# False.
#
# When checking, consider the number of characters needed to form the word,
# but ignore their case.
#
# Use the built-in Counter tool to solve this problem.
#


# Задача: "Скрэйббл"
# Реализуйте функцию-предикат scrabble, которая принимает на вход два
# параметра: набор символов (строку) и слово. Функция должна проверять,
# можно ли из переданного набора составить это слово. В результате вызова
# функция возвращает True или False.
#
# При проверке учитывается количество символов, которые нужны для составления
# слова, но не учитывается их регистр.
#
# Для решения используйте встроенный инструмент — Counter.


# Example:
# scrabble('rkqodlw', 'world')  # True
# scrabble('avj', 'java')  # False
# scrabble('avjafff', 'java')  # True
# scrabble('', 'hexlet')  # False
# scrabble('scriptingjava', 'JavaScript')  # True


from collections import Counter


def scrabble(string, word):
    char_set = dict(Counter(string.lower()))
    word_set = dict(Counter(word.lower()))

    for key, value in word_set.items():
        if key in char_set:
            if value > char_set[key]:
                return False
        else:
            return False
    return True

# Решение учителя:
# Можно было сделать ещё короче, если учесть то,
# как работает вычитание для пары Counter!
# Хватило бы: return not (Counter(word.lower()) - Counter(string.lower()))
