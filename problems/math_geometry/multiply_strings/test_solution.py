import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.multiply("2", "3") == "6"

    def test_example2(self):
        assert self.solution.multiply("123", "456") == "56088"
