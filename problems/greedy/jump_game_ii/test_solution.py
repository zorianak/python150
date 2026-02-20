import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.jump([2,3,1,1,4]) == 2

    def test_example2(self):
        assert self.solution.jump([2,3,0,1,4]) == 2
