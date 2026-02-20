import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.rob([1,2,3,1]) == 4

    def test_example2(self):
        assert self.solution.rob([2,7,9,3,1]) == 12
