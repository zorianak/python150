import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.minEatingSpeed([3,6,7,11], 8) == 4

    def test_example2(self):
        assert self.solution.minEatingSpeed([30,11,23,4,20], 5) == 30
