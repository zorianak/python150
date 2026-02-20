import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.maxCoins([3,1,5,8]) == 167

    def test_example2(self):
        assert self.solution.maxCoins([1,5]) == 10
