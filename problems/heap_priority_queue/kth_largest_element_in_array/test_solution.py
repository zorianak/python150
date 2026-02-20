import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.findKthLargest([3,2,1,5,6,4], 2) == 5

    def test_example2(self):
        assert self.solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
