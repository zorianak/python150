import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.uniquePaths(3, 7) == 28

    def test_example2(self):
        assert self.solution.uniquePaths(3, 2) == 3
