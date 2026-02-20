import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.findDuplicate([1,3,4,2,2]) == 2

    def test_example2(self):
        assert self.solution.findDuplicate([3,1,3,4,2]) == 3
