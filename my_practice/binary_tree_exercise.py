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


def solution(items: list[int]) -> list[list[int]]:
    tree = sorted_array_to_BST(items)
    result = []

    def walk(node, path):
        if not node.left and not node.right:
            result.append(path + [node.value])

        if node.left:
            walk(node.left, path + [node.value])
        if node.right:
            walk(node.right, path + [node.value])


    walk(tree, [])
    return result
