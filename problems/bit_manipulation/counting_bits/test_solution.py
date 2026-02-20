import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.countBits(2) == [0, 1, 1]

    def test_example2(self):
        assert self.solution.countBits(5) == [0, 1, 1, 2, 1, 2]
