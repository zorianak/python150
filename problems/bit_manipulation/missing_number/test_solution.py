import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.missingNumber([3,0,1]) == 2

    def test_example2(self):
        assert self.solution.missingNumber([0,1]) == 2
