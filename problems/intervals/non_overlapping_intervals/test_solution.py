import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1

    def test_example2(self):
        assert self.solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
