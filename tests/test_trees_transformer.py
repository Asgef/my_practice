from my_practice.trees_transformer import transform, tree_to_graph
from hexlet.graphs import sort_tree


def test_tree_to_graph():
    tree = ['A', [
        ['B', [['D']]],
        ['C', [['E'], ['F']]],
    ]]
    graph = {}
    tree_to_graph(tree, graph)
    expected = {
        'A': ['B', 'C'],
        'B': ['D', 'A'],
        'C': ['E', 'F', 'A'],
        'D': ['B'],
        'E': ['C'],
        'F': ['C'],
    }
    assert graph == expected


SIMPLE_TREE = ['A', [
    ['B', [
        ['D'],
    ]],
    ['C', [
        ['E'],
        ['F'],
    ]],
]]


def test_simple_1():
    expected = ['B', [
        ['A', [
            ['C', [
                ['E'],
                ['F'],
            ]],
        ]],
        ['D'],
    ]]
    actual = transform(SIMPLE_TREE, 'B')
    assert sort_tree(actual) == expected


TREE = ['A', [
    ['B', [
        ['D', [
            ['H'],
        ]],
        ['E'],
    ]],
    ['C', [
        ['F', [
            ['I', [
                ['M'],
            ]],
            ['J', [
                ['N'],
                ['O'],
            ]],
        ]],
        ['G', [
            ['K'],
            ['L'],
        ]],
    ]],
]]


def test_hard_1():
    expected = ['F', [
        ['C', [
            ['A', [
                ['B', [
                    ['D', [
                        ['H'],
                    ]],
                    ['E'],
                ]],
            ]],
            ['G', [
                ['K'],
                ['L'],
            ]],
        ]],
        ['I', [
            ['M'],
        ]],
        ['J', [
            ['N'],
            ['O'],
        ]],
    ]]
    actual = transform(TREE, 'F')
    assert sort_tree(actual) == expected


def test_hard_2():
    expected = ['I', [
        ['F', [
            ['C', [
                ['A', [
                    ['B', [
                        ['D', [
                            ['H'],
                        ]],
                        ['E'],
                    ]],
                ]],
                ['G', [
                    ['K'],
                    ['L'],
                ]],
            ]],
            ['J', [
                ['N'],
                ['O'],
            ]],
        ]],
        ['M'],
    ]]
    actual = transform(TREE, 'I')
    assert sort_tree(actual) == expected
