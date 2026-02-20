import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.findMedianSortedArrays([1,3], [2]) == 2.0

    def test_example2(self):
        assert self.solution.findMedianSortedArrays([1,2], [3,4]) == 2.5
