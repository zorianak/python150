import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.minCostClimbingStairs([10,15,20]) == 15

    def test_example2(self):
        assert self.solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6
