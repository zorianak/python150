import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.canJump([2,3,1,1,4]) == True

    def test_example2(self):
        assert self.solution.canJump([3,2,1,0,4]) == False
