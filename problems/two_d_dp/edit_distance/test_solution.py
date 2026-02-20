import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.minDistance("horse", "ros") == 3

    def test_example2(self):
        assert self.solution.minDistance("intention", "execution") == 5
