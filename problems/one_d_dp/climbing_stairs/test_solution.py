import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.climbStairs(2) == 2

    def test_example2(self):
        assert self.solution.climbStairs(3) == 3
