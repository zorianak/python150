import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.lastStoneWeight([2,7,4,1,8,1]) == 1

    def test_example2(self):
        assert self.solution.lastStoneWeight([1]) == 1
