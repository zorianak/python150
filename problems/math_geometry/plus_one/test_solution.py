import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.plusOne([1,2,3]) == [1, 2, 4]

    def test_example2(self):
        assert self.solution.plusOne([9]) == [1, 0]
