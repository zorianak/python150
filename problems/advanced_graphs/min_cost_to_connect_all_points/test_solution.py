import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20

    def test_example2(self):
        assert self.solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]]) == 18
