import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1, 6], [8, 10], [15, 18]]

    def test_example2(self):
        assert self.solution.merge([[1,4],[4,5]]) == [[1, 5]]
