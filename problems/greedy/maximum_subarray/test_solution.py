import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

    def test_example2(self):
        assert self.solution.maxSubArray([1]) == 1
