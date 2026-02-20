import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.minInterval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]) == [3, 3, 1, 4]

    def test_example2(self):
        assert self.solution.minInterval([[2,3],[2,5],[1,8],[20,25]], [2,19,22]) == [2, -1, 6]
