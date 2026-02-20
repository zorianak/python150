import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

    def test_example2(self):
        assert self.solution.trap([4,2,0,3,2,5]) == 9
