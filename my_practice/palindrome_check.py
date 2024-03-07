# Task: Palindrome Check

# Write a function to check if a string is a palindrome.
# That is, the string reads the same forwards and backwards.

# Examples:
# String 'qwertytrewq'
# Answer: True

# String 'qweqwtwe'
# Answer: False

# String 'anna'
# Answer: True

# String 'annet'
# Answer: False


# Задача: Проверка палиндрома

# Напишите функцию, которая проверяет, является ли строка палиндромом.
# То есть, строка читается слева направо и справа налево одинаково.

# Примеры:
# Строка 'qwertytrewq'
# Ответ: True

# Строка 'qweqwtwe'
# Ответ: False

# Строка 'anna'
# Ответ: True

# Строка 'annet'
# Ответ: False


def is_palindrome(text):
    front_pointer = 0
    rear_pointer = -1
    while front_pointer < len(text) // 2:
        if text[front_pointer] != text[rear_pointer]:
            return False

        front_pointer += 1
        rear_pointer -= 1

    return True
