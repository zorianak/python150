import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.maxProduct([2,3,-2,4]) == 6

    def test_example2(self):
        assert self.solution.maxProduct([-2,0,-1]) == 0
