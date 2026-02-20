import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.insert([[1,3],[6,9]], [2,5]) == [[1, 5], [6, 9]]

    def test_example2(self):
        assert self.solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1, 2], [3, 10], [12, 16]]
