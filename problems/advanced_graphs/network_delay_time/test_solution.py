import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2

    def test_example2(self):
        assert self.solution.networkDelayTime([[1,2,1]], 2, 1) == 1
