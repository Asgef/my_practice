# Задача: "Сумма интервалов"
# Реализуйте функцию `sum_of_intervals()`, которая принимает список интервалов
# и возвращает сумму длин всех интервалов. Перекрывающиеся интервалы должны
# учитываться только один раз.
#
#
# Task: "Sum of Intervals"
# Implement the function `sum_of_intervals()` that takes a list of intervals
# and returns the sum of all interval lengths. Overlapping intervals
# should only be counted once.
#
# Examples:
# from solution import sum_of_intervals
#
# sum_of_intervals([
#     [1, 1],
# ])  # 0
#
# sum_of_intervals([
#     [1, 2],
#     [50, 100],
#     [60, 70],
# ])  # 51
#
# sum_of_intervals([
#     [1, 2],
#     [5, 10],
# ])  # 6
#
# sum_of_intervals([
#     [1, 9],
#     [7, 12],
#     [3, 4],
# ])  # 11


def sum_of_intervals(intervals):
    values = []
    for start, end in intervals:
        for elm in range(start, end):
            if elm not in values:
                values.append(elm)
    return len(values)
