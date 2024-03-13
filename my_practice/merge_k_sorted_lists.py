# Task: Merge Sorted Lists

# You are given an array of k linked-lists lists, each linked-list
# is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []


# Задача: Слияние отсортированных списков

# Дан массив k связанных списков lists, каждый связанный список отсортирован
# по возрастанию.

# Объедините все связанные списки в один отсортированный
# связанный список и верните его.

# Пример 1:
# Ввод: lists = [[1,4,5], [1,3,4], [2,6]]
# Вывод: [1,1,2,3,4,4,5,6]
# Объяснение: Связанные списки:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# объединены в один отсортированный список:
# 1->1->2->3->4->4->5->6

# Пример 2:
# Ввод: lists = []
# Вывод: []

# Пример 3:
# Ввод: lists = [[]]
# Вывод: []


import heapq


def merge_lists(lists):
    min_heap = []
    result = []

    for idx, list_ in enumerate(lists):
        if list_:
            heapq.heappush(min_heap, (list_[0], idx, 0))

    while min_heap:
        value, list_idx, elem_idx = heapq.heappop(min_heap)
        result.append(value)
        if elem_idx + 1 < len(lists[list_idx]):
            next_elem = lists[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_elem, list_idx, elem_idx + 1))

    return result
