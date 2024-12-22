# Задача: "Перестроение дерева относительно заданного корневого узла"
# Реализуйте функцию `transform()`, которая перестраивает дерево так, чтобы
# указанный узел стал новым корнем, сохраняя связи между остальными узлами.
#
#
# Task: "Rebuilding a Tree Relative to a Given Root"
# Implement the function `transform()` that rebuilds a tree such that the specified
# node becomes the new root while preserving the relationships between all nodes.
#
#
# Example:
# Original tree:
# tree = ['A', [         #     A
#     ['B', [            #    / \
#         ['D'],         #   B   C
#     ]],                #  /   / \
#     ['C', [            # D   E   F
#         ['E'],
#         ['F'],
#     ]],
# ]]
#
# Call:
# transform(tree, 'B')
#
# Result:
# ['B', [                 #   B
#     ['D'],              #  / \
#     ['A', [             # D   A
#         ['C', [         #      \
#             ['E'],      #       C
#             ['F'],      #      / \
#         ]],             #     E   F
#     ]],
# ]]
#


def tree_to_graph(node: list, paths: dict) -> str:
    if len(node) == 1:
        point = node[0]
        paths[point] = []
        return point

    point, children = node
    paths[point] = []
    for child in children:
        neighbour = tree_to_graph(child, paths)
        paths[point].append(neighbour)
        paths[neighbour].append(point)
    return point


def tree_builder(start_node, graph, visited):
    visited.add(start_node)
    children = []
    for child in graph[start_node]:
        if child not in visited:
            children.append(list(tree_builder(child, graph, visited)))
    if children:
        return [start_node, children]
    return [start_node]


def transform(tree, node):
    adjacency_list = {}
    tree_to_graph(tree, adjacency_list)
    return tree_builder(node, adjacency_list, set())

