from my_practice.valid_parentheses import Solution


def test_valid_parentheses():
    solution = Solution()
    assert solution.isValid("()") is True
    assert solution.isValid("()[]{}") is True
    assert solution.isValid("(]") is False
    assert solution.isValid("([])") is True
    assert solution.isValid("{[]}") is True
    assert solution.isValid("[({})]") is True
    assert solution.isValid("((((") is False
    assert solution.isValid("({[)]}") is False
    assert solution.isValid("]") is False
    assert solution.isValid("){") is False
