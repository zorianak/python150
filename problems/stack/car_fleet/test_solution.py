import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3

    def test_example2(self):
        assert self.solution.carFleet(10, [3], [3]) == 1
