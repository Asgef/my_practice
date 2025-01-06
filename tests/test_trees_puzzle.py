from hexlet.graphs import sort_tree
from my_practice.trees_puzzle import combine


BRANCH1 = ['A', [
    ['B', [
        ['C'],
        ['D'],
    ]],
]]

BRANCH2 = ['B', [
    ['D', [
        ['E'],
        ['F'],
    ]],
]]

BRANCH3 = ['I', [
    ['A', [
        ['B', [
            ['C'],
            ['H'],
        ]],
    ]],
]]


def test_1():
    expected = ['A', [
        ['B', [
            ['C'],
            ['D', [
                ['E'],
                ['F'],
            ]],
            ['H'],
        ]],
        ['I'],
    ]]
    actual = combine(BRANCH1, BRANCH2, BRANCH3)
    assert sort_tree(actual) == expected


def test_2():
    expected = ['B', [
        ['A', [
            ['I'],
        ]],
        ['C'],
        ['D', [
            ['E'],
            ['F'],
        ]],
        ['H'],
    ]]
    actual = combine(BRANCH2, BRANCH1, BRANCH3)
    assert sort_tree(actual) == expected


def test_3():
    expected = ['I', [
        ['A', [
            ['B', [
                ['C'],
                ['D', [
                    ['E'],
                    ['F'],
                ]],
                ['H'],
            ]],
        ]],
    ]]
    actual = combine(BRANCH3, BRANCH2, BRANCH1)
    assert sort_tree(actual) == expected


def test_4():
    expected = ['B', [
        ['A', [
            ['I'],
        ]],
        ['C'],
        ['D', [
            ['E'],
            ['F'],
        ]],
        ['H'],
    ]]
    actual = combine(BRANCH2, BRANCH3)
    assert sort_tree(actual) == expected
