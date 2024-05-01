import os
from my_helper_code.parser import parse
from my_helper_code.data_loader import open_file
from my_practice.btrees_exercise import solution


test_dir = os.path.dirname(__file__)

file = os.path.join(test_dir, 'fixtures/b_tree.json')


def test_solution():

    case = parse(*open_file(file))
    expected = [30, 35, 38, 40, 42, 49, 50]

    assert solution(case, 30, 50) == expected
