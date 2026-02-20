import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4

    def test_example2(self):
        assert self.solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
