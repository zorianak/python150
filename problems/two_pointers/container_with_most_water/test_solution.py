import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49

    def test_example2(self):
        assert self.solution.maxArea([1,1]) == 1
