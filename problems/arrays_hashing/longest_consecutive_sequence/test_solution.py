import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.longestConsecutive([100,4,200,1,3,2]) == 4

    def test_example2(self):
        assert self.solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
