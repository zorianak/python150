import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.twoSum([2,7,11,15], 9) == [1, 2]

    def test_example2(self):
        assert self.solution.twoSum([2,3,4], 6) == [1, 3]
