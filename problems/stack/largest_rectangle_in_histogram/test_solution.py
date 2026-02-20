import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.largestRectangleArea([2,1,5,6,2,3]) == 10

    def test_example2(self):
        assert self.solution.largestRectangleArea([2,4]) == 4
