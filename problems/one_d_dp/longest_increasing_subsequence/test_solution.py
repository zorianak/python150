import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4

    def test_example2(self):
        assert self.solution.lengthOfLIS([0,1,0,3,2,3]) == 4
