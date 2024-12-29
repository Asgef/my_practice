# Задача: "Remove Invalid Parentheses"
# Реализовать функцию, которая принимает строку s, содержащую скобки и буквы.
# Функция должна удалить минимальное количество некорректных скобок,
# чтобы сделать строку валидной.
# Вернуть список уникальных валидных строк после минимальных удалений.
# Порядок в выходном списке может быть произвольным.
#
#
# Task: "Remove Invalid Parentheses"
# Implement a function that takes a string s containing parentheses and letters.
# The function should remove the minimum number of invalid parentheses to
# make the input string valid.
# Return a list of unique valid strings after the minimum number of removals.
# The order of the output list can be arbitrary.
#
# Examples:
# Input: s = "()())()"
# Output: ["(())()", "()()()"]
#
# Input: s = "(a)())()"
# Output: ["(a())()", "(a)()()"]
#
# Input: s = ")("
# Output: [""]
#


from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:  # noqa C901
        def is_valid(brackets) -> bool:
            balance = 0
            for bracket in brackets:
                if bracket == '(':
                    balance += 1
                elif bracket == ')':
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        def get_next(string):
            for idx, elem in enumerate(string):
                if elem not in '()':
                    continue
                yield f'{string[:idx]}{string[idx + 1:]}'

        result = set()
        candidates = {s}

        while not result:
            next_candidates = set()
            for candidate in candidates:
                if is_valid(candidate):
                    result.add(candidate)
                    continue
                next_candidates.update(get_next(candidate))
            candidates = next_candidates
        return list(result)
