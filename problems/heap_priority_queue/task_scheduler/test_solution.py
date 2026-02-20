import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.leastInterval(["A","A","A","B","B","B"], 2) == 8

    def test_example2(self):
        assert self.solution.leastInterval(["A","A","A","B","B","B"], 0) == 6
