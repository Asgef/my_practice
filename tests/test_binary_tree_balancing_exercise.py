import os
import pytest
from my_helper_code.parser import parse
from my_helper_code.data_loader import open_file
from my_practice.binary_tree_balancing_exercise import solution


test_dir = os.path.dirname(__file__)

file1 = os.path.join(test_dir, 'fixtures/tree_1.json')
file2 = os.path.join(test_dir, 'fixtures/tree_2.json')

case_1 = parse(*open_file(file1))
case_2 = parse(*open_file(file2))


@pytest.mark.parametrize('tree_data, expected_result', [
    (case_1, 1),
    (case_2, 2)
])
def test_solution(tree_data, expected_result):
    assert solution(tree_data) == expected_result
