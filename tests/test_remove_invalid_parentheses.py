import unittest
from my_practice.remove_invalid_parentheses import Solution


class TestRemoveInvalidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertCountEqual(
            self.solution.removeInvalidParentheses("()())()"),
            ["(())()", "()()()"]
        )

    def test_case_2(self):
        self.assertCountEqual(
            self.solution.removeInvalidParentheses("(a)())()"),
            ["(a())()", "(a)()()"]
        )

    def test_case_3(self):
        self.assertCountEqual(
            self.solution.removeInvalidParentheses(")("),
            [""]
        )

    def test_case_4(self):
        self.assertCountEqual(
            self.solution.removeInvalidParentheses("(((a))"),
            ["((a))"]
        )

    def test_case_5(self):
        self.assertCountEqual(
            self.solution.removeInvalidParentheses(""),
            [""]
        )
