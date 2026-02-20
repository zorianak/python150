import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]) == True

    def test_example2(self):
        assert self.solution.mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]) == False
