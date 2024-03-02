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
    word = ''
    state = 'outside_word'  # inside_word
    for string in data:
        print(string)
        for char in range(len(string)):
            symbol = string[char]
            print(symbol)
            if state == 'inside_word':
                if symbol == ' ' or symbol == '\n':
                    result.append(word)
                    word = ''
                    state = 'outside_word'
                    break
                word += symbol

            elif state == 'outside_word':
                if symbol == ' ' or symbol == '\n':
                    print('continue')
                    continue
                else:
                    state = 'inside_word'
                    word += symbol
    if word:
        result.append(word)
    return result


# data = [
#         '\n\n  hi   \n',
#         'hi how are you doing?\n',
#         ' hello',
#     ]
#
#
# print(solution(data))
