import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.characterReplacement("ABAB", 2) == 4

    def test_example2(self):
        assert self.solution.characterReplacement("AABABBA", 1) == 4
