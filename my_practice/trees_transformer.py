# Задача: "Перестроение дерева относительно заданного корневого узла"
# Реализуйте функцию `transform()`, которая перестраивает дерево так, чтобы
# указанный узел стал новым корнем, сохраняя связи между остальными узлами.
#
#
# Task: "Rebuilding a Tree Relative to a Given Root"
# Implement the function `transform()` that rebuilds a tree such that
# the specified
# node becomes the new root while preserving
# the relationships between all nodes.
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


import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


def tree_to_graph(node: list, path: dict) -> str:
    if len(node) == 1:
        value_node = node[0]
        path[value_node] = []
        return value_node
    value_node, children = node
    path[value_node] = []
    for child in children:
        neighbor = tree_to_graph(child, path)
        path[value_node].append(neighbor)
        path[neighbor].append(value_node)
    return value_node


def graph_to_tree(start_node: str, path: dict, visited: set) -> list:
    visited.add(start_node)
    children = []
    for neighbour in path[start_node]:
        if neighbour not in visited:
            children.append(graph_to_tree(neighbour, path, visited))
    if children:
        return [start_node, children]
    return [start_node]


def transform(tree: list[str, list], node: str) -> list:
    adjacency_list = {}
    tree_to_graph(tree, adjacency_list)
    new_tree = graph_to_tree(node, adjacency_list, set())
    return new_tree
