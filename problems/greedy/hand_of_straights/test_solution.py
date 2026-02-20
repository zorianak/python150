import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.isNStraightHand([1,2,3,6,2,3,4,7,8], 3) == True

    def test_example2(self):
        assert self.solution.isNStraightHand([1,2,3,4,5], 4) == False
