import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]) == 4

    def test_example2(self):
        assert self.solution.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]) == 4
