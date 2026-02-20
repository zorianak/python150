import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"

    def test_example2(self):
        assert self.solution.minWindow("a", "a") == "a"
