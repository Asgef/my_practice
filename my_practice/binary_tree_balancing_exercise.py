from hexlet_code.helpers import build_RBTree

# Напишите функцию, которая возвращает черную высоту дерева.
# Предполагаем, что дерево сбалансированно.
#
#          5b
#        /   \
#       /     \
#      3r      8r
#     / \     / \
#    2b 4b   7b 9b
#   /       /
#  1r      6r
#
# solution(tree) # 1

# Для преобразования исходного массива в дерево используйте функцию
# build_RBTree()
#
# def solution(data):
#     tree = build_RBTree(data)
#     return count_black_nodes(tree)  ## функция, которую вам нужно реализовать
#
# solution(data) ## 1


def count_black_nodes(node, depth=0, acc=0):
    if node is None:
        return acc

    if node.is_red is False and depth > 0:
        return count_black_nodes(node.left, **{'depth': depth+1, 'acc': acc+1})

    return count_black_nodes(node.left, **{'depth': depth + 1, 'acc': acc})


def solution(data):
    tree = build_RBTree(data)
    return count_black_nodes(tree)
