from hexlet_code.helpers import sorted_array_to_BST


#  Напишите функцию для бинарного дерева поиска, которая выводит все пути
#  от корня до листовых узлов.
#
#          5
#        /   \
#       /     \
#      3       8
#     / \     / \
#    2   4   7   9
#   /       /
#  1       6

# из дерева выше должен получиться массив с массивами всех путей
# Для преобразования исходного массива в дерево используйте
# функцию sorted_array_to_BST()
#
# [
#     [5, 3, 2, 1],
#     [5, 3, 4],
#     [5, 8, 7, 6],
#     [5, 8, 9],
# ]


def solution(items):
    result = []
    tree = sorted_array_to_BST(items)

    def walk(node, acc):
        if node is None:
            return acc
        acc.append(node.value)
        left_node = walk(node.left, acc.copy())
        if left_node:
            result.append(left_node)
            return
        walk(node.right, acc.copy())

    walk(tree, [])
    return result
