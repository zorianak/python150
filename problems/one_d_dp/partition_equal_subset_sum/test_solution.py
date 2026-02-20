import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.canPartition([1,5,11,5]) == True

    def test_example2(self):
        assert self.solution.canPartition([1,2,3,5]) == False
