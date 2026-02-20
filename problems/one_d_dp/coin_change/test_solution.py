import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.coinChange([1,2,5], 11) == 3

    def test_example2(self):
        assert self.solution.coinChange([2], 3) == -1
