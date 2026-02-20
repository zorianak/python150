import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.evalRPN(["2","1","+","3","*"]) == 9

    def test_example2(self):
        assert self.solution.evalRPN(["4","13","5","/","+"]) == 6
