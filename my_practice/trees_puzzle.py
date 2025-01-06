# Задача: "Пазл"
# Реализуйте функцию combine(), которая объединяет ветки в одно дерево.
# Каждая ветка представляет собой дерево. Корнем итогового дерева становится
# корневой узел первой переданной ветки.
#
#
# Task: "Puzzle"
# Implement the combine() function that merges branches into one tree.
# Each branch is a tree, and the root of the merged tree becomes the root of
# the first passed branch.
#
# Example:
#
# branch1 = ['A', [
#     ['B', [
#         ['C'],
#         ['D'],
#     ]],
# ]]
#
# branch2 = ['B', [
#     ['D', [
#         ['E'],
#         ['F'],
#     ]],
# ]]
#
# branch3 = ['I', [
#     ['A', [
#         ['B', [
#             ['C'],
#             ['H'],
#         ]],
#     ]],
# ]]
#
# combine(branch1, branch2, branch3)
# Result:
# ['A', [
#     ['B', [
#         ['C'],
#         ['D', [
#             ['E'],
#             ['F'],
#         ]],
#         ['H'],
#     ]],
#     ['I'],
# ]]


from my_practice.trees_transformer import graph_to_tree


def tree_to_graph(node: list, paths: dict) -> str:
    if len(node) == 1:
        node_value = node[0]
        paths.setdefault(node_value, [])
        return node_value

    node_value, children = node
    paths.setdefault(node_value, [])

    for child in children:
        neighbour = tree_to_graph(child, paths)
        paths[node_value].append(neighbour)
        paths[neighbour].append(node_value)
    return node_value


def combine(*branches: list) -> list:
    first_node = branches[0][0]
    adjacency_list = {}
    for branch in branches:
        tree_to_graph(branch, adjacency_list)
    new_tree = graph_to_tree(first_node, adjacency_list, set())
    return new_tree
