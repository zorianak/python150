import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.twoSum([2, 7, 11, 15], 9) == [0, 1]

    def test_example2(self):
        assert self.solution.twoSum([3, 2, 4], 6) == [1, 2]
