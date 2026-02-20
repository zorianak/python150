import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.productExceptSelf([1,2,3,4]) == [24, 12, 8, 6]

    def test_example2(self):
        assert self.solution.productExceptSelf([-1,1,0,-3,3]) == [0, 0, 9, 0, 0]
