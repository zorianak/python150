import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.rob([2,3,2]) == 3

    def test_example2(self):
        assert self.solution.rob([1,2,3,1]) == 4
