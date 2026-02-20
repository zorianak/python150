import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.search([-1,0,3,5,9,12], 9) == 4

    def test_example2(self):
        assert self.solution.search([-1,0,3,5,9,12], 2) == -1
