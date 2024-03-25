# Problem: String comparison using a stack
#
# Implement a function that compares two strings and returns true if they
# are equal. The "#" character means a backspace character. The function
# should compare the final state of the two strings after all backspaces
# have been applied. If the final states are equal, return true, otherwise
# return false.
# Example usage:
# solution('ab#c', 'ad#c') # Returns true
# solution('ab##', 'c#d#') # Returns true
# solution('a#c', 'b') # Returns false

# Задача: Сравнение строк с использованием стека
#
# Реализуйте функцию, которая сравнивает две строки и возвращает true, если
# они равны. Символ "#" означает символ бэкспейса.
# Функция должна сравнивать конечное состояние двух
# строк после применения всех бэкспейсов. Если конечные состояния равны,
# верните true, в противном случае верните false.
# Пример использования:
# stack_lexem('ab#c', 'ad#c') # Возвращает true
# stack_lexem('ab##', 'c#d#') # Возвращает true
# stack_lexem('a#c', 'b') # Возвращает false


def process_string(text):
    stack = []
    for char in text:
        if char != '#':
            stack.append(char)
        elif stack:
            stack.pop()
    return ''.join(stack)


def stack_lexem(a, b):
    res_a = process_string(a)
    res_b = process_string(b)
    return res_a == res_b
