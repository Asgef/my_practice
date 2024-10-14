# Task: Valid Parentheses
#
# Given a string 's' containing only the characters '(', ')', '{', '}', '['
# and ']', determine if the input string is valid.
#
# A string is valid if:
# 1. Open brackets are closed by the same type of brackets.
# 2. Open brackets are closed in the correct order.
# 3. Every closing bracket has a corresponding open bracket of the same type.
#
#
# Задача: Допустимые скобки
#
# Дана строка 's', содержащая только символы '(', ')', '{', '}', '[' и ']'.
# Определите, является ли строка допустимой.
#
# Строка считается допустимой, если:
# 1. Открытые скобки закрываются скобками того же типа.
# 2. Открытые скобки закрываются в правильном порядке.
# 3. Каждой закрывающейся скобке соответствует открывающаяся того же типа.
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Example 4:
# Input: s = "([])"
# Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        MAPPING = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if not stack and char in MAPPING:
                return False

            if char not in MAPPING:
                stack.append(char)
                continue

            if stack[-1] != MAPPING[char]:
                return False
            stack.pop()

        return not stack

# Стек.
