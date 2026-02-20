import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.findTargetSumWays([1,1,1,1,1], 3) == 5

    def test_example2(self):
        assert self.solution.findTargetSumWays([1], 1) == 1
