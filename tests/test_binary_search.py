from my_practice.binary_search import binary_search


def test_binary_search():
    assert binary_search([-5, 2, 4, 6, 9], 4) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([], 1) == -1
    assert binary_search([3], 3) == 0
    assert binary_search([1, 2, 3, 4, 5], -1) == -1
