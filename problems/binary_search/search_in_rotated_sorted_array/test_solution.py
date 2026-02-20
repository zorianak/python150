import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.search([4,5,6,7,0,1,2], 0) == 4

    def test_example2(self):
        assert self.solution.search([4,5,6,7,0,1,2], 3) == -1
