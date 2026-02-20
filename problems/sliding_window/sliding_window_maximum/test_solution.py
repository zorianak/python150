import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3, 3, 5, 5, 6, 7]

    def test_example2(self):
        assert self.solution.maxSlidingWindow([1], 1) == [1]
