import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.maxProfit([7,1,5,3,6,4]) == 5

    def test_example2(self):
        assert self.solution.maxProfit([7,6,4,3,1]) == 0
