# Problem: Finite Automaton Lexer
#
# Implement a function that takes text as input and returns an array consisting
# of the first words of each line of text. Empty lines should be ignored.
#
# Lines are separated by line breaks.
# Any number of spaces may appear anywhere in a line.
# Text must be processed character by character (we are writing a lexer).
#
# Example:
# const text = '  what who   \nhellomy\n hello who are you\n';
# const result = solution(text);
# // [
# //   'what',
# //   'hellomy',
# //   'hello',
# // ];
#
# The solution must be finite automaton-based.
from django.db.models.expressions import result

from tests.test_prefix_tree_exercise import words


# Задача: Автоматный лексер
#
# Реализуйте функцию, которая принимает на вход текст и возвращает массив,
# состоящий из первых слов каждой строки текста. Пустые строчки должны быть
# проигнорированы.
#
# Строки разделяются переводом строки.
# В любом месте строки может быть сколько угодно пробелов.
# Текст должен перебираться посимвольно (мы пишем лексер).
#
# Пример:
# const text = '  what who   \nhellomy\n hello who are you\n';
# const result = solution(text);
# // [
# //   'what',
# //   'hellomy',
# //   'hello',
# // ];
#
# Решение должно быть автоматным.


def solution(data):
    result = []
    state = 'outside_word'  # inside_word

    for string in data:
        word = ''

        for idx in range(len(string)):
            symbol = string[idx]

            if state == 'inside_word':
                if symbol == ' ' or symbol == '\n':
                    result.append(word)
                    word = ''
                    state = 'outside_word'
                    break
                word += symbol

            elif state == 'outside_word':
                if symbol != ' ' and symbol != '\n':
                    state = 'inside_word'
                    word += symbol
                else:
                    continue

        if word:
            result.append(word)

    return result


def lexer(text: str) -> list:
    result = []
    text_array = []
    state = 'outside_word'  # inside_word
    word_ln = ''

    for char in text:
        if char == '\n':
            text_array.append(word_ln)
            word_ln = ''
        else:
            word_ln += char
    text_array.append(word_ln)


    for line in text_array:
        word = ''
        for idx in range(len(line)):
            symbol = line[idx]

            if state == 'inside_word':
                if symbol == ' ':
                    result.append(word)
                    word = ''
                    state = 'outside_word'
                    break
                word += symbol

            elif state == 'outside_word':
                if symbol != ' ':
                    state = 'inside_word'
                    word += symbol
                else:
                    continue
        state = 'outside_word'


        if word:
            result.append(word)

    return result

# TODO: Требуется пересмотреть решение
