import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.myPow(2.00000, 10) == 1024.0

    def test_example2(self):
        assert self.solution.myPow(2.10000, 3) == 9.261000000000001
