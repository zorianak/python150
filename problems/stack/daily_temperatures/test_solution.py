import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1, 1, 4, 2, 1, 1, 0, 0]

    def test_example2(self):
        assert self.solution.dailyTemperatures([30,40,50,60]) == [1, 1, 1, 0]
