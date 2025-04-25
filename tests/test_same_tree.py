from my_practice.same_tree import Solution
from hexlet_code.helpers import build_BinaryTree


def test_is_same_tree():
    s = Solution()
    assert s.isSameTree(build_BinaryTree([1, 2, 3]), build_BinaryTree([1, 2, 3])) is True
    assert s.isSameTree(build_BinaryTree([1, 2]), build_BinaryTree([1, None, 2])) is False
    assert s.isSameTree(build_BinaryTree([1, 2, 1]), build_BinaryTree([1, 1, 2])) is False
    assert s.isSameTree(None, None) is True
    assert s.isSameTree(build_BinaryTree([1]), None) is False
    assert s.isSameTree(None, build_BinaryTree([1])) is False
    assert s.isSameTree(build_BinaryTree([42]), build_BinaryTree([42])) is True
    assert s.isSameTree(build_BinaryTree([1]), build_BinaryTree([2])) is False
