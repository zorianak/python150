import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True

    def test_example2(self):
        assert self.solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False
